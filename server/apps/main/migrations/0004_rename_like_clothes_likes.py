# Generated by Django 3.2 on 2023-02-10 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_clothes_rem_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='like',
            new_name='likes',
        ),
    ]
