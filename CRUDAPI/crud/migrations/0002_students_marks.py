# Generated by Django 4.2.6 on 2023-10-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='marks',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
