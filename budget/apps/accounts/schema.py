import graphene

from graphene_django import DjangoObjectType

from .models import Account
from budget.utils.decorators import permissions_classes
from budget.utils.permissions import IsAuthenticated


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class AccountInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    type = graphene.String(required=True)
    institution = graphene.String(required=True)
    description = graphene.String(required=False)
    amount = graphene.Decimal(required=False)
    number = graphene.String(required=False)


class CreateAccount(graphene.Mutation):
    class Arguments:
        account_data = AccountInput(required=True)

    success = graphene.Boolean()
    account = graphene.Field(AccountType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, account_data=None):
        user = info.context.user or None
        account = Account(**account_data, user=user)
        success = True
        account.save()

        return CreateAccount(account=account, success=success)


class EditAccount(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        account_data = AccountInput(required=True)

    success = graphene.Boolean()
    account = graphene.Field(AccountType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        account = Account.objects.get(pk=kwargs.get("id"), user=user)
        account_data = kwargs.get("account_data")
        for key, value in account_data.items():
            setattr(account, key, value)
        account.save()

        success = True

        return EditAccount(account=account, success=success)


class QueryAccount(object):
    all_accounts = graphene.List(AccountType)
    account = graphene.Field(
        AccountType,
        id=graphene.ID(required=False),
        account_number=graphene.String(required=False),
    )

    @permissions_classes([IsAuthenticated])
    def resolve_account(self, info, **kwargs):
        user = info.context.user or None
        id = kwargs.get("id")
        account_number = kwargs.get("account_number")

        if id is not None:
            return Account.objects.get(pk=id, user=user)
        if account_number is not None:
            return Account.objects.get(number=account_number, user=user)

        return None

    @permissions_classes([IsAuthenticated])
    def resolve_all_accounts(self, info, **kwargs):
        user = info.context.user or None
        return Account.objects.filter(user=user)


class AccountMutation(graphene.ObjectType):
    create_account = CreateAccount.Field()
    edit_account = EditAccount.Field()
