import graphene

from graphene_django import DjangoObjectType

from .models import Budget

class BudgetType(DjangoObjectType):
  class Meta:
    model = Budget

class BudgetMutation(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    
  success = graphene.Boolean()
  budget = graphene.Field(BudgetType)

  def mutate(self, info, name, description):
    budget = Budget(
      name=name,
      description=description
    )
    success = True
    budget.save()

    return BudgetMutation(budget=budget, success=success)

class BudgetMutation(graphene.ObjectType):
  create_budget = BudgetMutation.Field()
