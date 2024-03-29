# Generated by Django 4.2.6 on 2023-10-31 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('taken', models.BooleanField(default=False)),
                ('returned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=120)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.books')),
            ],
        ),
    ]
