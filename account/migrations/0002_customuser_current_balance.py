# Generated by Django 2.1.7 on 2019-11-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='current_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
