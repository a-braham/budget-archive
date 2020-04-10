import graphene

from graphene_django import DjangoObjectType

from .models import Account
from budget.apps.authentication.schema import UserType
from budget.util.decorators import permissions_classes
from budget.util.permissions import IsAuthenticated


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class CreateAccount(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        type = graphene.String(required=True)
        institution = graphene.String(required=True)
        description = graphene.String(required=False)
        amount = graphene.String(required=False)
        number = graphene.String(required=False)

    success = graphene.Boolean()
    account = graphene.Field(AccountType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        account = Account(
            **kwargs,
            user=user
        )
        success = True
        account.save()

        return CreateAccount(account=account, success=success)


class AccountMutation(graphene.ObjectType):
    create_account = CreateAccount.Field()
