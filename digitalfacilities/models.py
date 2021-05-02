from django.db import models

# Create your models here.


GREETING_CARD_CATEGORY = (
    ("Christmas", "Christmas"),
    ("New Year", "New Year"),
    ("Marriage", "Marriage"),
    ("Birthday", "Birthday"),
    ("My Cards", "My Cards"),
)

VISITING_CARD_CATEGORY = (
    ("Business", "Business"),
    ("Corporate", "Corporate"),
    ("Festive", "Festive"),
    ("Store", "Store"),
    ("My Cards", "My Cards"),
)


class DigitalDiary(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to="DigitalFacilities/DigitalDiary", blank=True)
    start_date = models.DateField()
    description = models.TextField()
    reminder = models.BooleanField(default=True)
    days_left = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class DigitalGreetingCard(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    sender = models.CharField(max_length=60, help_text='From')
    receiver = models.CharField(max_length=60, help_text='To')
    message = models.TextField()
    category = models.CharField(max_length=60, choices=GREETING_CARD_CATEGORY)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class DigitalVisitingCard(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    business_name = models.CharField(max_length=120)
    your_name = models.CharField(max_length=80)
    email = models.EmailField()
    designation = models.CharField(max_length=120)
    contact_no = models.CharField(max_length=12)
    address = models.CharField(max_length=180)
    website = models.URLField()
    image = models.ImageField(upload_to="DigitalFacilities/DigitalVisitingCard", blank=True)
    category = models.CharField(max_length=60, choices=VISITING_CARD_CATEGORY)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
