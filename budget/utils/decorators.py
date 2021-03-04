from .exceptions import PermissionDenied


def permissions_classes(permissions, manually=False):
    """
    Run the permissions provided
    """

    def wrapper(func):
        def inner(cls, info, *args, **kwargs):
            if check_permissions(permissions, info.context):
                length(cls, info, *args, **kwargs)
                return func(cls, info, **kwargs)
            raise PermissionDenied("Permission Denied!")

        return inner

    return wrapper


def length(cls, info, *args, **kwargs):
    if len(args) > 0:
        id = args[0]
        obj = cls._meta.model.objects.get(pk=id)
        permissions = kwargs.pop("permissions")
        if check_obj_permissions(permissions, info.context, obj):
            manual(cls, info, *args, **kwargs)
        else:
            raise PermissionDenied("Permission Denied!")


def manual(cls, info, *args, **kwargs):
    manually = kwargs.pop("manually")
    func = kwargs.pop("func")
    if manually:
        return func(info, *args, **kwargs)
    return func(cls, info, *args, **kwargs)


def check_permissions(permissions, context):
    """
    Check permissions and raise exception
    """
    for permission in permissions:
        if not permission.has_permission(context):
            return False
        return True


def check_obj_permissions(permissions, context, obj):
    """
    Check permissions for obj. Riase exception
    """
    for permission in permissions:
        if not permission.has_obj_permission(context, obj):
            return False
        return True
