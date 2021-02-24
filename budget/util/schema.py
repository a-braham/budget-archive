import graphene
from .types import ExpectedErrorType


class Output:
    """
    Base class for response outputs. All classes extend this class
    """

    success = graphene.Boolean(default_value=True)
    errors = graphene.Field(ExpectedErrorType)
