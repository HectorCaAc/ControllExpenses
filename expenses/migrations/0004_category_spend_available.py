# Generated by Django 2.1.7 on 2019-11-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20191117_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='spend_available',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
