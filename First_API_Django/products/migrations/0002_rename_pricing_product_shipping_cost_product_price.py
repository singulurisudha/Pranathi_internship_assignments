# Generated by Django 4.2.5 on 2023-10-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pricing',
            new_name='shipping_cost',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
