import graphene

from graphene_django import DjangoObjectType

from budget.util.decorators import permissions_classes
from budget.util.permissions import IsAuthenticated
from .models import Profile


class ProfileType(DjangoObjectType):
    """
    Profile types from profile models
    """

    class Meta:
        """
        Associated profiles models
        """

        model = Profile


class ProfileInput(graphene.InputObjectType):
    """
    Inputs: profile fields
    """

    phone_number = graphene.String(required=True)
    first_name = graphene.String(required=True)
    middle_name = graphene.String(required=False)
    last_name = graphene.String(required=True)
    bio = graphene.String(required=False)
    picture = graphene.String(required=False)


class UpdateProfile(graphene.Mutation):
    """
    UPDATE: profiles mutations
    """

    class Arguments:
        """
        Associated arguments for editing profile
        """

        profile_data = ProfileInput(required=True)

    success = graphene.Boolean()
    profile = graphene.Field(ProfileType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, **kwargs):
        user = info.context.user or None
        profile = Profile.objects.get(user=user)
        profile_data = kwargs.get("profile_data")
        for key, value in profile_data.items():
            setattr(profile, key, value)
        profile.save()

        success = True

        return UpdateProfile(profile=profile, success=success)


class QueryProfile(object):
    """
    Get: one and all profiles
    """

    all_profiles = graphene.List(ProfileType)
    profile = graphene.Field(
        ProfileType,
        id=graphene.ID(required=False),
        phone_number=graphene.String(required=False),
    )

    @permissions_classes([IsAuthenticated])
    def resolve_profile(self, info, **kwargs):
        user = info.context.user or None
        id = kwargs.get("id")
        phone_number = kwargs.get("profile_number")

        if id is not None:
            return Profile.objects.get(pk=id, user=user)
        if phone_number is not None:
            return Profile.objects.get(number=phone_number, user=user)

        return None


class ProfileMutation(graphene.ObjectType):
    """
    All profile mutations
    """

    update_profile = UpdateProfile.Field()
