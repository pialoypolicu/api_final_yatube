# Generated by Django 3.2.3 on 2021-06-02 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]