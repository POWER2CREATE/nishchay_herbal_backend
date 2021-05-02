from django.db import models

# Create your models here.


class Product(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    product_name = models.CharField(max_length=80)
    product_image1 = models.ImageField(blank=True, upload_to="Ecommerce/Products", null=True)
    product_image2 = models.ImageField(blank=True, upload_to="Ecommerce/Products", null=True)
    product_image3 = models.ImageField(blank=True, upload_to="Ecommerce/Products", null=True)
    product_image4 = models.ImageField(blank=True, upload_to="Ecommerce/Products", null=True)
    product_image5 = models.ImageField(blank=True, upload_to="Ecommerce/Products", null=True)
    product_mrp = models.IntegerField()
    selling_price = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    in_stock = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Nischay Herbal Products'

    def __str__(self):
        return str(self.product_name)


class RatingReview(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    rating = models.IntegerField()
    review = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Rating & Reviews'

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)
