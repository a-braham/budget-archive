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

    def mutate(self, info, **kwargs):
        user = User(**kwargs)
        user.set_password(kwargs.get("password"))
        user.save()

        return CreateUser(user=user)


class AuthMutation(graphene.ObjectType):
    register = CreateUser.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
