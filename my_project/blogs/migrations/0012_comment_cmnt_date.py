# Generated by Django 3.1.3 on 2020-12-14 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cmnt_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
