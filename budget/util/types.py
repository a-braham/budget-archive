import graphene
from graphene_django.utils import camelize

from .exceptions import WrongUsage

class ExpectedErrorType(graphene.Scalar):
  class Meta:
    description = """
    Error messages mapped to fields and non fields errors
    {
        field_name: [
            {
                "message": "error message",
                "code": "error_code"
            }
        ],
        other_field: [
            {
                "message": "error message",
                "code": "error_code"
            }
        ],
        nonFieldErrors: [
            {
                "message": "error message",
                "code": "error_code"
            }
        ]
    }
    """

    @staticmethod
    def serialize(errors):
      if isinstance(errors, dict):
        if errors.get('__all__', False):
          errors['non_field_errors'] = errors.pop('__all__')
        return camelize(errors)
      elif isinstance(errors, list):
        return {'nonFieldErrors': errors}
      raise WrongUsage('`errors` must be list or dict!')
