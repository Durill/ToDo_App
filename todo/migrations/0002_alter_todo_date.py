# Generated by Django 4.2.2 on 2023-06-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(),
        ),
    ]