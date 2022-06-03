from csv import reader
from typing import Dict

from django.core.management import BaseCommand

from points.models import TypeOfPointsModel, PointModel


class Command(BaseCommand):
    CSV_NAME_TO_TYPE_OF_POINTS_NAME = {
        "ZACISKANIE NA CZAS": "ZACISKANIE KABLA NA CZAS",
        "PYTANIE": "PRELEKCYJNE PYTANIA",
    }

    def add_arguments(self, parser):
        parser.add_argument("-f", type=str, help="file path", required=True)

    def handle(self, *args, **options):
        file_path = options.get("f")

        NAME_TO_TYPE_OF_POINTS: Dict[
            str, TypeOfPointsModel
        ] = TypeOfPointsModel.objects.all().in_bulk(field_name="name")

        to_create = []

        with open(file_path, "r") as file:
            csv_reader = reader(file)
            next(csv_reader)  # ignore header

            for row in csv_reader:
                if not row or not row[0]:
                    print("ignoring row", row)
                    continue

                name = row[0]
                label = row[1]
                try:
                    points = int(row[2])
                except ValueError:
                    print("-ignoring row", row)
                    continue
                type_of_points_name: str = self.CSV_NAME_TO_TYPE_OF_POINTS_NAME.get(
                    name, name
                )
                type_of_points: TypeOfPointsModel = NAME_TO_TYPE_OF_POINTS[
                    type_of_points_name
                ]
                code = row[3]

                to_create.append(
                    PointModel(
                        code=code,
                        value=points,
                        type_of_points=type_of_points,
                        description=label,
                    )
                )
        print("len(to_create)", len(to_create), "codes")
        PointModel.objects.bulk_create(to_create, ignore_conflicts=True)
        print("PointModel.objects.count()", PointModel.objects.count())
