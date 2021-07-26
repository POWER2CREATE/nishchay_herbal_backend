# Generated by Django 3.1.4 on 2021-07-24 09:04

from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20210723_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.jobrecruiter'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(upload_to='Job/Resume/', validators=[job.models.validate_file_extension]),
        ),
    ]