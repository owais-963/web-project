# Generated by Django 3.1.4 on 2020-12-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20201229_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='adrress',
            new_name='adress',
        ),
    ]
