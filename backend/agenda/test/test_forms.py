from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.test import TestCase

# Create your tests here.

from agenda.factories import UserFactory, RoomModelFactory, LectureModelFactory
from agenda.forms import LectureForm
from agenda.models import LectureModel
from pages.helpers import clean_html


class LectureFormTest(TestCase):
    def setUp(self):
        self.username = "user_1"
        self.password = "password_1"
        self.user: User = UserFactory(
            username=self.username, email="email@domain.com", password=self.password
        )
        RoomModelFactory()
        self.room = RoomModelFactory()

    def test_create_new_object(self):
        data = {
            "author": "author 0",
            "description": "<p>description 0</p><script>alert(1)</script>",
            "start_date": "2019-08-05 21:22",
            "end_date": "2019-08-05 22:22",
            "room": self.room.pk,
        }

        form = LectureForm(data=data)
        self.assertTrue(form.is_valid())
        lecture: LectureModel = form.save()

        self.assertEqual(lecture.author, data["author"])
        expected_description = "<p>description 0</p>alert(1)"
        self.assertEqual(expected_description, lecture.description)
        self.assertEqual(lecture.description, clean_html(data["description"]))
        self.assertEqual(lecture.room.pk, self.room.pk)

    def test_create_new_object_wrong_date(self):
        data = {
            "author": "author 0",
            "description": "<script>alert(1)</script><p>description 0</p>",
            "start_date": "2019-08-05 21:22",
            "end_date": "2019-08-05 20:22",
            "room": self.room.pk,
        }

        form = LectureForm(data=data)
        self.assertFalse(form.is_valid())
        errors = form.errors.get_json_data()
        self.assertEqual(
            errors["end_date"][0]["message"],
            "End date must be greater than start date.",
        )

    def test_update_object_with_xss(self):
        lecture = LectureModelFactory()

        data: dict = model_to_dict(lecture)
        data["description"] = "<script>console.log(123)</script>"

        form = LectureForm(data=data, instance=lecture)
        self.assertTrue(form.is_valid())
        form.save()

        lecture.refresh_from_db()
        expected_description = "console.log(123)"
        self.assertEqual(lecture.description, expected_description)
