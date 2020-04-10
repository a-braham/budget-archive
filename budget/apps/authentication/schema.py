from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql_auth import mutations

User = get_user_model()

class UserType(DjangoObjectType):
  class Meta:
    model = User

class CreateUser(graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    phone_number = graphene.String(required=True)
    first_name = graphene.String(required=False)
    middle_name = graphene.String(required=False)
    last_name = graphene.String(required=False)
    password = graphene.String(required=True)
  
  class Meta:
    user = graphene.Field(UserType)

  def mutate(self, info, username, email, phone_number, password, **kwargs):
    user = User(
      username = username,
      email = email,
      phone_number = phone_number,
      **kwargs
    )
    user.set_password(password)
    user.save()

    return CreateUser(user=user)

class AuthMutation(graphene.ObjectType):
  register = CreateUser.Field()
  verify_account = mutations.VerifyAccount.Field()
  token_auth = mutations.ObtainJSONWebToken.Field()
  update_account = mutations.UpdateAccount.Field()

