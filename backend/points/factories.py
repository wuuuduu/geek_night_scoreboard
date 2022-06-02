import factory

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils.timezone import now

from points.models import PlayerModel, TypeOfPointsModel, PointModel


class PlayerModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = PlayerModel

    username = factory.Sequence(lambda n: "username_%d" % n)


class TypeOfPointsModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = TypeOfPointsModel

    name = factory.Sequence(lambda n: "type_name_%d" % n)


class PointModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = PointModel

    value = factory.Iterator([100, 200, 500])
    code = factory.Sequence(lambda n: "code_%d" % n)
    type_of_points = factory.SubFactory(TypeOfPointsModelFactory)
    description = factory.Sequence(lambda n: "description_%d" % n)
