# Generated by Django 3.1.3 on 2020-12-07 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20201208_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]