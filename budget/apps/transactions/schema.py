import graphene

from graphene_django import DjangoObjectType

from .models import Transaction

class TransactionType(DjangoObjectType):
  class Meta:
    model = Transaction

class TransactionMutation(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    
  success = graphene.Boolean()
  transaction = graphene.Field(TransactionType)

  def mutate(self, info, name, description):
    transaction = Transaction(
      name=name,
      description=description
    )
    success = True
    transaction.save()

    return TransactionMutation(transaction=transaction, success=success)

class TransactionMutation(graphene.ObjectType):
  create_transaction = TransactionMutation.Field()
