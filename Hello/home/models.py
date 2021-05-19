from django.db import models

# Contact Form Models from Contact Us page
class Contact(models.Model):
    name = models.CharField(max_length=122)
    name1 = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    date = models.DateField()
    def __str__(self):
        return self.name


# Product Database
class Product(models.Model):
    Age_Choices = [
        ('0', 'Upto 6 months'),
        ('1', 'Upto 1 years'),
        ('2', 'Upto 2 years'),
        ('3', 'Upto 3 years'),
        ('4', 'Upto 4 years'),
        ('5', 'Upto 5 years'),
        ('6', 'Upto 6 years'),
    ]
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    baby_age = models.CharField(
        max_length=20,
        choices=Age_Choices,
        default='0',
    )
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=122)
    most_popular = models.BooleanField(default=False)
    hot_selling = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.product_name
    
    