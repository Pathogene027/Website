from .models import Product

#I) Inserting a new record

x = Product(product_name = 'Cerelac', product_manu_date=2019-4-10, product_exp_date=2025-10-20)
x.save()

#II) Get all the records in the Product Table

all_record = Product.objects.all()
all_record

#III) Filter products by their name

the_product = Product.objects.filter(product_name='Cerelac')
the_product

#IV) Get a single record from product table

the_product = Product.object.get(pk = 1)

#v) Change a product price
x = Product.objects.filter(product_name = 'Rice').last()
x.product_price = 20
x.save()

