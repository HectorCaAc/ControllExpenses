# Generated by Django 2.1.7 on 2019-11-17 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20191116_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='surplus',
            new_name='deficit',
        ),
    ]
