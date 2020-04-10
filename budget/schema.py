import graphene

from graphql_auth.schema import UserQuery, MeQuery

import budget.apps.authentication.schema
import budget.apps.budget.scheme
import budget.apps.categories.schema

class Query(UserQuery, MeQuery, graphene.ObjectType):
  pass

class Mutation(
  budget.apps.authentication.schema.AuthMutation,
  budget.apps.budget.scheme.BudgetMutation,
  budget.apps.categories.schema.CategoryMutation,
  graphene.ObjectType
  ):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
