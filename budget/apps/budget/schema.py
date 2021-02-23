import graphene

from graphene_django import DjangoObjectType

from .models import Budget
from budget.util.decorators import permissions_classes
from budget.util.permissions import IsAuthenticated
from budget.apps.categories.models import Category


class BudgetInput(graphene.InputObjectType):
    amount = graphene.Decimal(required=True)
    description = graphene.String(required=False)


class BudgetType(DjangoObjectType):
    class Meta:
        model = Budget


class CreateBudget(graphene.Mutation):
    class Arguments:
        category_id = graphene.ID(required=True)
        budget_data = BudgetInput(required=True)

    success = graphene.Boolean()
    budget = graphene.Field(BudgetType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, budget_data=None, **kwargs):
        user = info.context.user or None
        category_id = kwargs.get("category_id")

        category = Category.objects.get(pk=category_id, user=user) or None

        budget = Budget(**budget_data, user=user, category=category)
        success = True
        budget.save()

        return CreateBudget(budget=budget, success=success)


class UpdateBudget(graphene.Mutation):
    class Arguments:
        budget_id = graphene.ID(required=True)
        budget_data = BudgetInput(required=True)

    success = graphene.Boolean()
    budget = graphene.Field(BudgetType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        budget = Budget.objects.get(pk=kwargs.get("budget_id"), user=user)
        budget_data = kwargs.get("budget_data")
        for key, value in budget_data.items():
            setattr(budget, key, value)
        budget.save()

        success = True

        return UpdateBudget(budget=budget, success=success)


class QueryBudget(object):
    all_budgets = graphene.List(BudgetType)
    budget = graphene.Field(
        BudgetType,
        budget_id=graphene.ID(required=False),
        budget_reference=graphene.String(required=False),
    )

    @permissions_classes([IsAuthenticated])
    def resolve_budget(self, info, **kwargs):
        user = info.context.user or None
        budget_id = kwargs.get("budget_id")

        if budget_id is not None:
            return Budget.objects.get(pk=budget_id, user=user)
        return None

    @permissions_classes([IsAuthenticated])
    def resolve_all_budgets(self, info, **kwargs):
        user = info.context.user or None
        return Budget.objects.filter(user=user)


class BudgetMutation(graphene.ObjectType):
    create_budget = CreateBudget.Field()
    update_budget = UpdateBudget.Field()
