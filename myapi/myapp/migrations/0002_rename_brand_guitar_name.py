# Generated by Django 3.2.5 on 2021-07-16 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guitar',
            old_name='brand',
            new_name='name',
        ),
    ]
