from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from points.factories import (
    PlayerModelFactory,
    TypeOfPointsModelFactory,
    PointModelFactory,
)
from points.models import PointModel, PlayerModel, TypeOfPointsModel


class PointModelFormTest(TestCase):
    def setUp(self):
        self.type_of_points: TypeOfPointsModel = TypeOfPointsModelFactory(
            name="Informerzy"
        )
        self.player: PlayerModel = PlayerModelFactory()
        self.player_2: PlayerModel = PlayerModelFactory()
        self.points_1: PointModel = PointModelFactory(
            type_of_points=self.type_of_points
        )
        self.points_2: PointModel = PointModelFactory(
            type_of_points=self.type_of_points
        )
        self.points_3: PointModel = PointModelFactory(
            type_of_points=self.type_of_points
        )

    def test_correct_request(self):
        data = {"acquired_by_player": self.player.pk, "code": self.points_1.code}
        self.assertEqual(self.points_1.acquired_by_player, None)
        client = Client()
        response = client.post(reverse("points:add_points_view"), data=data)
        self.assertEqual(response.status_code, 302)
        self.points_1.refresh_from_db()
        self.assertEqual(self.points_1.acquired_by_player, self.player)

    def test_incorrect_request(self):
        # check if user can steal points of other user

        self.points_1.acquired_by_player = self.player_2
        self.points_1.save()
        data = {"acquired_by_player": self.player.pk, "code": self.points_1.code}
        self.assertEqual(self.points_1.acquired_by_player, self.player_2)
        client = Client()
        response = client.post(reverse("points:add_points_view"), data=data)
        self.assertEqual(response.status_code, 200)
        self.points_1.refresh_from_db()
        self.assertEqual(self.points_1.acquired_by_player, self.player_2)
