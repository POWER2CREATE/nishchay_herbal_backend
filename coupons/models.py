from django.db import models
import secrets
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    user = models.ForeignKey('core.User', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.code

REWARD_TYPE = (
    ('None', 'None'),
    ('Coupon', 'Coupon'),
    ('Product', 'Product'),
)

class Reward(models.Model):
    user = models.ManyToManyField('core.User')
    type_rew = models.CharField(choices=REWARD_TYPE, max_length=20)
    coupon = models.OneToOneField(Coupon, on_delete=models.CASCADE, null=True)
    product = models.OneToOneField('ecommerce.Product', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user) + " " + self.type_rew

class RewardSystem(models.Model):
    user = models.ForeignKey('core.User',on_delete=models.PROTECT)
    points = models.PositiveIntegerField(default=0)
    claims = models.PositiveIntegerField(default=0)
    totalReferral = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Reward System'
    
    def __str__(self):
        return str(self.user)

class RewardCode(models.Model):

    code = models.CharField(max_length=10)
    user = models.ForeignKey('core.User',on_delete=models.PROTECT)
    max_discount = models.PositiveIntegerField()
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

