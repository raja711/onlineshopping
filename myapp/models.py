from django.db import models

# Create your models here.
class registertbl(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.username

# यह प्रोडक्ट मॉडल जोड़ें ताकि सर्च काम कर सके
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


