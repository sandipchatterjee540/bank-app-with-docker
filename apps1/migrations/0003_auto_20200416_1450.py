# Generated by Django 3.0.5 on 2020-04-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps1', '0002_auto_20200416_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createacount',
            name='sax',
            field=models.CharField(max_length=10),
        ),
    ]
