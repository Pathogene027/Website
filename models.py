from django.db import models


# Create your models here.
class People(models.Model):
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    email = models.EmailField()
    time_on_log = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fname} {self.sname}'


class Address(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    citizenship = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    GPS_post_code = models.CharField(max_length=50)

    def __str__(self):
        return f'Address'


class Doctor(models.Model):
    people = models.OneToOneField(People, on_delete=models.CASCADE)
    Doc_fname = models.CharField(max_length=50)
    Doc_sname = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.fname} {self.sname}'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_manu_date = models.DateField()
    product_exp_date = models.DateField()
    product_price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.product_name}'


class Bio(models.Model):
    bio = models.CharField(max_length=1000)
    people = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bio}'
