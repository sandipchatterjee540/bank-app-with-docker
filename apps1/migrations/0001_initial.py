# Generated by Django 3.0.5 on 2020-04-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAcount',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=12)),
                ('money', models.IntegerField()),
                ('sax', models.CharField(max_length=4)),
                ('date', models.DateField()),
            ],
        ),
    ]
