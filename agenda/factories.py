import factory

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils.timezone import now

from agenda.models import RoomModel, LectureModel


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Sequence(lambda n: "First_name_%d" % n)
    last_name = factory.Sequence(lambda n: "Last_name_%d" % n)
    email = factory.Sequence(lambda n: "email_%d@domain.com" % n)
    username = factory.Sequence(lambda n: 'username_%d' % n)
    password = 'pass'

    @factory.post_generation
    def set_password(self, create, extracted, **kwargs):
        self.set_password(self.password)


class RoomModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = RoomModel

    name = factory.Sequence(lambda n: "room_%d" % n)


class LectureModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = LectureModel

    author = factory.Sequence(lambda n: "author_%d" % n)
    description = factory.Sequence(lambda n: "description_%d" % n)
    start_date = factory.Sequence(lambda n: now() + timedelta(hours=n))
    end_date = factory.Sequence(lambda n: now() + timedelta(hours=n + 1))
    room = factory.SubFactory(RoomModelFactory)
