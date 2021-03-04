import graphene

from graphene_django import DjangoObjectType

from .models import Category
from budget.utils.decorators import permissions_classes
from budget.utils.permissions import IsAuthenticated


class CategoryInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    type = graphene.String(required=True)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput(required=True)

    success = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, category_data=None):
        user = info.context.user or None
        category = Category(**category_data, user=user)
        success = True
        category.save()

        return CreateCategory(category=category, success=success)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        category_data = CategoryInput(required=True)

    success = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    @permissions_classes([IsAuthenticated])
    def mutate(self, info, **kwargs):
        category = Category.objects.get(pk=kwargs.get("id"))
        category_data = kwargs.get("category_data")

        for key, value in category_data.items():
            setattr(category, key, value)
        category.save()
        success = True

        return UpdateCategory(category=category, success=success)


class QueryCategory(object):
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(
        CategoryType,
        id=graphene.ID(required=False),
    )

    @permissions_classes([IsAuthenticated])
    def resolve_category(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Category.objects.get(pk=id)
        return None

    @permissions_classes([IsAuthenticated])
    def resolve_all_categories(self, info, **kwargs):
        user = info.context.user or None
        return Category.objects.filter(user=user)


class CategoryMutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
