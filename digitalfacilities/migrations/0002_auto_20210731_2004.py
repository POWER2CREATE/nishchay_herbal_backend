# Generated by Django 3.1.4 on 2021-07-31 14:34

import digitalfacilities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalfacilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitaldiary',
            name='start_date',
            field=models.DateField(validators=[digitalfacilities.models.no_past]),
        ),
    ]
