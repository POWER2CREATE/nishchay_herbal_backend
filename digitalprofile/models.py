from django.db import models

# Create your models here.


class DigitalProfile(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    company_name = models.CharField(max_length=60)
    company_logo = models.ImageField(upload_to="DigitalProfile/Company/")
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.company_name)


class PersonalDetail(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    digital_profile = models.OneToOneField(DigitalProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=12)
    designation = models.CharField(max_length=30)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=13)
    address = models.CharField(max_length=80)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=40)
    about_us = models.TextField(max_length=180)

    def __str__(self):
        return str(self.digital_profile)


class SocialMediaLinks(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    other_link = models.URLField(blank=True)

    def __str__(self):
        return str(self.digital_profile)


class PaymentDetail(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE)
    paytm_number = models.CharField(max_length=13, blank=True)
    paytm_qr_code = models.ImageField(blank=True, upload_to="DigitalProfile/PaymentDetail/")
    google_pay_number = models.CharField(max_length=13, blank=True)
    google_pay_qr_code = models.ImageField(blank=True, upload_to="DigitalProfile/PaymentDetail/")
    phonepe_number = models.CharField(max_length=13, blank=True)
    phonepe_qr_code = models.ImageField(blank=True, upload_to="DigitalProfile/PaymentDetail/")
    account_number = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=50)
    re_account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=50)
    gst_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.digital_profile)


class Services(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE)
    service_name1 = models.CharField(max_length=50)
    service_image1 = models.ImageField(blank=True, upload_to="DigitalProfile/Services/")
    service_name2 = models.CharField(max_length=50, blank=True)
    service_image2 = models.ImageField(blank=True, upload_to="DigitalProfile/Services/")
    service_name3 = models.CharField(max_length=50, blank=True)
    service_image3 = models.ImageField(blank=True, upload_to="DigitalProfile/Services/")

    def __str__(self):
        return str(self.digital_profile)


class Ecommerce(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE)
    product_image = models.ImageField(blank=True, upload_to="DigitalProfile/Ecommerce/")
    product_name = models.CharField(max_length=60)
    product_mrp = models.IntegerField()
    selling_price = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=180)

    def __str__(self):
        return str(self.digital_profile)


class Gallery(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="DigitalProfile/Gallery/")
    image2 = models.ImageField(upload_to="DigitalProfile/Gallery", blank=True)
    image3 = models.ImageField(upload_to="DigitalProfile/Gallery", blank=True)
    image4 = models.ImageField(upload_to="DigitalProfile/Gallery", blank=True)
    image5 = models.ImageField(upload_to="DigitalProfile/Gallery", blank=True)

    def __str__(self):
        return str(self.digital_profile)
