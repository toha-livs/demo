# Generated by Django 2.0.1 on 2018-01-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('vote', models.TextField()),
            ],
        ),
    ]
