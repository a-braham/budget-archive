import graphene

from graphene_django import DjangoObjectType

from .models import Transaction
from budget.util.decorators import permissions_classes
from budget.util.permissions import IsAuthenticated
from budget.apps.budget.models import Budget
from budget.apps.categories.models import Category
from budget.apps.accounts.models import Account
from budget.util.exceptions import TransactionError


class TransactionInput(graphene.InputObjectType):
    reference = graphene.String(required=True)
    type = graphene.String(required=True)
    amount = graphene.Decimal(required=True)
    description = graphene.String(required=False)


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction


class CreateTransaction(graphene.Mutation):
    class Arguments:
        category_id = graphene.ID(required=False)
        account_id = graphene.ID(required=False)
        budget_id = graphene.ID(required=False)
        transaction_data = TransactionInput(required=True)

    success = graphene.Boolean()
    transaction = graphene.Field(TransactionType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, transaction_data=None, **kwargs):
        user = info.context.user or None
        category_id = kwargs.get("category_id")
        account_id = kwargs.get("account_id")
        budget_id = kwargs.get("budget_id")

        category = Category.objects.filter(pk=category_id, user=user).first()
        account = Account.objects.filter(pk=account_id, user=user).first()
        budget = Budget.objects.filter(pk=budget_id, user=user).first()
        if category is None and account is None and budget is None:
            raise TransactionError

        transaction = Transaction(
            **transaction_data,
            user=user,
            category=category,
            account=account,
            budget=budget,
        )
        success = True
        transaction.save()

        return CreateTransaction(transaction=transaction, success=success)


class UpdateTransaction(graphene.Mutation):
    class Arguments:
        transaction_id = graphene.ID(required=True)
        transaction_data = TransactionInput(required=True)

    success = graphene.Boolean()
    transaction = graphene.Field(TransactionType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        transaction = Transaction.objects.get(
            pk=kwargs.get("transaction_id"), user=user
        )
        transaction_data = kwargs.get("transaction_data")
        for key, value in transaction_data.items():
            setattr(transaction, key, value)
        transaction.save()

        success = True

        return UpdateTransaction(transaction=transaction, success=success)


class QueryTransaction(object):
    all_transactions = graphene.List(TransactionType)
    transaction = graphene.Field(
        TransactionType,
        transaction_id=graphene.ID(required=False),
        transaction_reference=graphene.String(required=False),
    )

    @permissions_classes([IsAuthenticated])
    def resolve_transaction(self, info, **kwargs):
        user = info.context.user or None
        transaction_id = kwargs.get("transaction_id")
        transaction_reference = kwargs.get("transaction_reference")

        if transaction_id is not None:
            return Transaction.objects.get(pk=transaction_id, user=user)
        if transaction_reference is not None:
            reference = transaction_reference
            return Transaction.objects.get(reference=reference, user=user)

        return None

    @permissions_classes([IsAuthenticated])
    def resolve_all_transactions(self, info, **kwargs):
        user = info.context.user or None
        return Transaction.objects.filter(user=user)


class TransactionMutation(graphene.ObjectType):
    create_transaction = CreateTransaction.Field()
    update_transaction = UpdateTransaction.Field()
