# Generated by Django 3.1.4 on 2021-06-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalprofile',
            name='company_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='description',
            field=models.TextField(max_length=180),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='product_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='account_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='branch_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='google_pay_number',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='gst_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='paytm_number',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='phonepe_number',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='re_account_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='about_us',
            field=models.TextField(max_length=180),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='address',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='designation',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='whatsapp',
            field=models.CharField(max_length=13),
        ),
    ]
