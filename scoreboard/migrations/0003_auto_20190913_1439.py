# Generated by Django 2.2.3 on 2019-09-13 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_auto_20190913_1335'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LectureModel',
        ),
        migrations.DeleteModel(
            name='RoomModel',
        ),
    ]
