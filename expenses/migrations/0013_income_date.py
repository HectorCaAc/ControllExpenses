# Generated by Django 3.0.3 on 2020-03-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0012_auto_20191212_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
