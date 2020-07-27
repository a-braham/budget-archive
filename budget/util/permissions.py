from graphene_django import DjangoObjectType

from .decorators import permissions_classes


class BasePermissions:
    """
    Class base permissions from which all permissions inherit
    """
    @staticmethod
    def has_permission(context):
        """
        Return `True` if permission is granted else `False`
        """
        return True

    @staticmethod
    def has_object_permission(context, obj):
        """
        Return `True` if object permission is granted else `False`
        """
        return True


class IsAuthenticated(BasePermissions):
    """
    Allows access to authenticated users only
    """
    @staticmethod
    def has_permission(context):
        return context.user and context.user.is_authenticated


class AllowAny(BasePermissions):
    """
    Allow access to all
    """
    @staticmethod
    def has_permission(context):
        return True
