import factory
from factory.django import DjangoModelFactory

from points.models import PlayerModel, TypeOfPointsModel, PointModel


class PlayerModelFactory(DjangoModelFactory):
    class Meta:
        model = PlayerModel

    username = factory.Sequence(lambda n: "username_%d" % n)


class TypeOfPointsModelFactory(DjangoModelFactory):
    class Meta:
        model = TypeOfPointsModel

    name = factory.Sequence(lambda n: "type_name_%d" % n)


class PointModelFactory(DjangoModelFactory):
    class Meta:
        model = PointModel

    value = factory.Iterator([100, 200, 500])
    code = factory.Sequence(lambda n: "code_%d" % n)
    type_of_points = factory.SubFactory(TypeOfPointsModelFactory)
    description = factory.Sequence(lambda n: "description_%d" % n)
