import graphene

from graphene_django import DjangoObjectType

from .models import Category

class CategoryType(DjangoObjectType):
  class Meta:
    model = Category

class CategoryMutation(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    
  success = graphene.Boolean()
  category = graphene.Field(CategoryType)

  def mutate(self, info, name, description):
    category = Category(
      name=name,
      description=description
    )
    success = True
    category.save()

    return CategoryMutation(category=category, success=success)

class CategoryMutation(graphene.ObjectType):
  create_category = CategoryMutation.Field()
