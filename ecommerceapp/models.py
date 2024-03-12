from django.db import models

# Create your models here.

class sregmodels(models.Model):
    sname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    cname=models.CharField(max_length=30)
    tl=models.CharField(max_length=30)
    caddress=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=30)

class sregmodelview(models.Model):
    sname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    cname=models.CharField(max_length=30)
    tl=models.CharField(max_length=30)
    caddress=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    imgup=models.FileField(upload_to='ecommerceapp/static')
    def __str__(self):
        return self.sname


class itemup(models.Model):
    pimage=models.FileField(upload_to='ecommerceapp/static')
    pname=models.CharField(max_length=50)
    price=models.IntegerField()
    pdes=models.CharField(max_length=50)
    choice=[
        ('coffee','coffee'),
        ('cpowders','cpowders'),
        ('cmugs','cmugs'),
        ('camchines','cmachines'),
        ('cblenders','cblenders')


    ]
    category=models.CharField(max_length=50,choices=choice)
    # def __str__(self):
    #     return self.pname


class buyerregmodel(models.Model):
    pimg=models.FileField(upload_to='ecommerceapp/static')
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    uname=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.fname


class wishlist(models.Model):
    product_image=models.FileField()
    userid = models.IntegerField()
    product_name=models.CharField(max_length=50)
    prod_price=models.IntegerField()
    prod_description=models.CharField(max_length=50)
    prod_category=models.CharField(max_length=50)
    prod_id=models.IntegerField()
    def __str__(self):
        return self.product_name

class cart(models.Model):
    kimage=models.FileField()
    kuserid=models.IntegerField()
    kprod_id=models.IntegerField()
    kprodname=models.CharField(max_length=30)
    kprodprice=models.IntegerField()
    kproddes=models.CharField(max_length=30)
    kprodcat=models.CharField(max_length=30)
    quantity=models.IntegerField()
    def __str__(self):
        return self.kprodname

class delivery(models.Model):
    name=models.CharField(max_length=50)
    pin=models.IntegerField()
    delivery_add=models.CharField(max_length=50)
    phone=models.IntegerField()
    streetname=models.CharField(max_length=50)
    userid=models.IntegerField()
    choice=[
        ('Kerala','Kerala'),
        ('Tamilnadu','Tamilnadu'),
        ('Karnataka','Karnataka')
    ]
    state=models.CharField(max_length=50,choices=choice)
    choice1=[
        ('Kerala','Kerala'),
        ('UnitedState','UnitedState'),
        ('Canada','Canada')

    ]
    country=models.CharField(max_length=50,choices=choice1)



class confirmmodel(models.Model):
    userid=models.IntegerField()
    address=models.CharField(max_length=400)
    prodimg=models.FileField()
    prod_details=models.CharField(max_length=400)
    totalprice=models.IntegerField()
    order_date=models.DateField(auto_now_add=True)
    estimated_date=models.DateField()


class cart_details(models.Model):
    userid = models.IntegerField()
    prod_img=models.CharField(max_length=100)
    booking_date=models.DateField()
    amount=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pin=models.IntegerField()
    def __str__(self):
        return self.street


class cardmodel(models.Model):
    userid=models.IntegerField()
    prod_img=models.CharField(max_length=100)
    booking_date=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pin=models.IntegerField()
    cardname=models.CharField(max_length=50)
    cardno=models.CharField(max_length=50)
    expiry=models.CharField(max_length=50)
    cvv=models.CharField(max_length=50)
    def __str__(self):
        return self.cardname



class place_order(models.Model):
    userid = models.IntegerField()
    prod_name=models.CharField(max_length=50)
    booked_date=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    card_number=models.CharField(max_length=50)
    expiry=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)

#class based model

class clregmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)





