from django.db import models

# Create your models here.


CATEGORY = (
    ('Advocate', 'Advocate'),
    ('Beauty Parlour', 'Beauty Parlour'),
    ('Cake Shop', 'Cake Shop'),
    ('Gym', 'Gym'),
    ('Visiting Card', 'Visiting Card'),
    ('Coffee', 'Coffee'),
    ('Teacher', 'Teacher'),
    ('Ac Repair', 'AC Repair'),
    ('Wedding Card', 'Wedding Card'),
    ('Flowers', 'Flowers'),
    ('Gifts', 'Gifts'),
)


class VendorServicesName(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)


class Vendor(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    email = models.EmailField(null=True)
    address_line_1 = models.CharField(max_length=180, null=True)
    address2_line_2 = models.CharField(max_length=180, null=True)
    city = models.CharField(max_length=60, null=True)
    state = models.CharField(max_length=60, null=True)
    pincode = models.IntegerField(null=True)

    category = models.CharField(max_length=40, choices=CATEGORY, null=True)
    gstin = models.CharField(max_length=60, null=True)
    business_address_line_1 = models.CharField(max_length=180, null=True)
    business_address2_line_2 = models.CharField(max_length=180, null=True)
    business_city = models.CharField(max_length=60, null=True)
    business_city_pincode = models.IntegerField(null=True)
    business_state = models.CharField(max_length=60, null=True)
    country = models.CharField(max_length=60, null=True)
    image = models.ImageField(blank=True, upload_to="Vendor/Business", null=True)
    address_proof_image = models.ImageField(blank=True, upload_to="Vendor/Business", null=True)

    account_holder_name = models.CharField(max_length=50, null=True)
    account_number = models.CharField(max_length=40, null=True)
    re_account_number = models.CharField(max_length=40, null=True)
    ifsc_code = models.CharField(max_length=20, null=True)
    branch_name = models.CharField(max_length=60, null=True)
    pancard_holder_name = models.CharField(max_length=40, null=True)
    pancard_number = models.CharField(max_length=40, null=True)
    services = models.ManyToManyField(VendorServicesName, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


"""class BusinessInformation(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    category = models.CharField(max_length=40, choices=CATEGORY)
    gstin = models.CharField(max_length=60)
    address_line_1 = models.CharField(max_length=180)
    address2_line_2 = models.CharField(max_length=180)
    city = models.CharField(max_length=60)
    pincode = models.IntegerField()
    state = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    image = models.ImageField(blank=True, upload_to="Vendor/Business", null=True)
    address_proof_image = models.ImageField(blank=True, upload_to="Vendor/Business", null=True)

    def __str__(self):
        return str(self.vendor)"""


"""class BankDetails(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=40)
    re_account_number = models.CharField(max_length=40)
    ifsc_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=60)
    pancard_holder_name = models.CharField(max_length=40)
    pancard_number = models.CharField(max_length=40)

    def __str__(self):
        return str(self.vendor)"""


"""class VendorServices(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    services = models.ManyToManyField(VendorServicesName, blank=True)

    def __str__(self):
        return str(self.vendor)"""
