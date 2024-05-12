from turtle import mode
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
category_choices=(
        ("Smartphone","Smartphone"),
        ("SmartTv","SmartTv"),
        ("Laptop","Laptop"),
        ("Headphone","Headphone"),
        ("SmartWatch","SmartWatch"),
        ("Camera","Camera"),
        ("Speaker","Speaker"),
    )
country_choices=(
        ("India","India"),
    )
state_choices =(
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Chandigarh","Chandigarh"),
    )

class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='User')
    add_count=models.SmallIntegerField(default=0,verbose_name='Address count')
    name=models.CharField(max_length=100,verbose_name='name',null=False)
    phone=models.CharField(max_length=14,verbose_name='phone_number')
    email=models.EmailField(max_length=30,null=True,verbose_name='Email address')
    address=models.CharField(max_length=200,verbose_name='Address',null=False)
    country=models.CharField(max_length=10,choices = country_choices,verbose_name='Country')
    state=models.CharField(max_length=30,choices = state_choices,verbose_name='State')
    city=models.CharField(max_length=50,verbose_name='City')
    zipcode=models.PositiveIntegerField(verbose_name='Zipcode')
    is_selected=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class product(models.Model):
    title=models.CharField(max_length=100,verbose_name='title')
    sell_price=models.FloatField(verbose_name='Selling_price')
    discount_price=models.FloatField(verbose_name='discount_price')
    description=models.TextField(verbose_name='Description')
    brand=models.CharField(max_length=50,verbose_name='Brand')
    category=models.CharField(max_length=30,choices = category_choices,verbose_name='Category')
    product_image=models.ImageField(upload_to='product_image', max_length=100,verbose_name='Product_image')
    is_trendy=models.BooleanField(default=False)
    is_new=models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.product_image.path) # Open image using self

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.product_image.path)  # saving image at the same path

class orderplaced(models.Model):
    status_choices=(
        ("Order placed","Order placed"),
        ("On the way","On the way"),
        ("shipped","shipped"),
        ("Out for delievery","Out for delivery"),
        ("Delivered","Delivered"),
        ("Canceled","Canceled"),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='User')
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True,verbose_name='Product')
    address_details=models.TextField(null=True,verbose_name="Adddress Details")
    quantity=models.PositiveSmallIntegerField(default=1,verbose_name='Quantity')
    total_amount=models.FloatField(default=0,verbose_name='Total amount')
    ordered_date=models.DateField(null=True,verbose_name='Order date')
    status=models.CharField(max_length=30,choices=status_choices,verbose_name='Status',default='Order placed')

    def __str__(self):
        return str(self.user)

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='User')
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True,verbose_name='Product')
    quantity=models.PositiveSmallIntegerField(default=1,verbose_name='Quantity')
    pending = models.BooleanField(default=True)
    price=models.FloatField(verbose_name='total_price',null=True)

    def __str__(self):
        return str(self.user)