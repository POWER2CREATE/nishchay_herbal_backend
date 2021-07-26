# Generated by Django 3.1.4 on 2021-07-23 16:15

from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20210607_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.jobrecruiter', validators=[job.models.validate_file_extension]),
        ),
    ]