# Generated by Django 4.2.6 on 2023-10-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_students_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='marks',
            field=models.IntegerField(null=True),
        ),
    ]
