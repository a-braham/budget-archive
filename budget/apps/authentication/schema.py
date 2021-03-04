from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

import graphene
from graphene_django import DjangoObjectType
from graphql_auth import mutations

from graphql_auth.models import UserStatus

from rest_framework import exceptions
from rest_framework.authtoken.models import Token

from budget.utils.mailers import VerificationMail
from budget.utils.decorators import permissions_classes
from budget.utils.permissions import IsAuthenticated
from budget.utils.auth_handlers import AuthTokenHandler

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    class Meta:
        user = graphene.Field(UserType)

    def mutate(self, info, **kwargs):
        user = User(**kwargs)
        user.set_password(kwargs.get("password"))
        user.save()
        token = AuthTokenHandler.create_auth_token(user)
        VerificationMail(user, token.key).send_mail()

        return CreateUser(user=user, token=token)


class VerifyUser(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    success = graphene.Boolean()
    user = graphene.Field(UserType)
    message = graphene.String()

    def mutate(self, info, token):
        try:
            token = Token.objects.get(key=token)
            user = token.user
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed(
                "Invalid Token. The token provided cannot be decoded!"
            )
        if AuthTokenHandler.expired_token(token):
            raise exceptions.AuthenticationFailed(
                "The token used has expired. Please authenticate again!"
            )
        UserStatus.objects.filter(user=user).update(verified=True)

        success = True
        message = "Your email is verified"

        return VerifyUser(user=user, success=success, message=message)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @permissions_classes([IsAuthenticated])
    def resolve_users(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication Failure: Your must be signed in")
        if user.is_staff is False:
            raise Exception("Authentication Failure: Must be a staff")
        return User.objects.all()


class AuthMutation(graphene.ObjectType):
    register = CreateUser.Field()
    verify_user = VerifyUser.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
