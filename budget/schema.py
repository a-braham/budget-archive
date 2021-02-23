import graphene

from graphql_auth.schema import UserQuery, MeQuery

import budget.apps.authentication.schema
import budget.apps.budget.schema
import budget.apps.accounts.schema
import budget.apps.transactions.schema
import budget.apps.categories.schema
import budget.apps.profiles.schema


class Query(
    UserQuery,
    MeQuery,
    graphene.ObjectType,
    budget.apps.accounts.schema.QueryAccount,
    budget.apps.transactions.schema.QueryTransaction,
    budget.apps.categories.schema.QueryCategory,
    budget.apps.budget.schema.QueryBudget,
    budget.apps.profiles.schema.QueryProfile,
):
    pass


class Mutation(
    budget.apps.authentication.schema.AuthMutation,
    budget.apps.budget.schema.BudgetMutation,
    budget.apps.accounts.schema.AccountMutation,
    budget.apps.transactions.schema.TransactionMutation,
    budget.apps.categories.schema.CategoryMutation,
    budget.apps.profiles.schema.ProfileMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
