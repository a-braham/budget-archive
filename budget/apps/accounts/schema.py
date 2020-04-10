import graphene

from graphene_django import DjangoObjectType

from .models import Account

class AccountType(DjangoObjectType):
  class Meta:
    model = Account

class AccountMutation(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    
  success = graphene.Boolean()
  account = graphene.Field(AccountType)

  def mutate(self, info, name, description):
    account = Account(
      name=name,
      description=description
    )
    success = True
    account.save()

    return AccountMutation(account=account, success=success)

class AccountMutation(graphene.ObjectType):
  create_account = AccountMutation.Field()
