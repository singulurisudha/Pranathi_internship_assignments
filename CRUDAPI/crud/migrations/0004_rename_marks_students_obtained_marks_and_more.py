# Generated by Django 4.2.6 on 2023-10-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_students_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='marks',
            new_name='obtained_marks',
        ),
        migrations.AddField(
            model_name='students',
            name='total_marks',
            field=models.IntegerField(null=True),
        ),
    ]
