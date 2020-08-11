import graphene

from graphql_auth.schema import UserQuery, MeQuery

import budget.apps.authentication.schema
import budget.apps.budget.scheme
import budget.apps.categories.schema
import budget.apps.accounts.schema
import budget.apps.transactions.schema


class Query(
    UserQuery,
    MeQuery,
    graphene.ObjectType,
    budget.apps.accounts.schema.QueryAccount,
    budget.apps.transactions.schema.QueryTransaction,
):
    pass


class Mutation(
    budget.apps.authentication.schema.AuthMutation,
    budget.apps.budget.scheme.BudgetMutation,
    budget.apps.categories.schema.CategoryMutation,
    budget.apps.accounts.schema.AccountMutation,
    budget.apps.transactions.schema.TransactionMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
