# Generated by Django 2.2.3 on 2019-09-14 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecturemodel',
            options={'ordering': ('order',), 'verbose_name': 'Lecture', 'verbose_name_plural': 'Lectures'},
        ),
        migrations.AlterModelOptions(
            name='roommodel',
            options={'ordering': ('order',), 'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
        migrations.AlterField(
            model_name='lecturemodel',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='lecturemodel',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_set', to='agenda.RoomModel'),
        ),
    ]
