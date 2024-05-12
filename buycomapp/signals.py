from django.dispatch import receiver
from django.core.signals import request_finished
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.contrib.auth.models import User
from .models import cart


@receiver(request_finished)
def notify_request(sender,**kwargs):
    print("request finished")

@receiver(user_logged_in,sender=User)
def notify_userlogin(sender,request,user,**kwargs):
    print("User logged in")

@receiver(user_logged_out,sender=User)
def notify_userlogout(sender,request,user,**kwargs):
    print("User logged out")

@receiver(user_login_failed,sender=User)
def notify_userlogin_failed(sender,request,user,**kwargs):
    print("User login failed")


@receiver(post_save,sender=cart)
def notify_cart_add(sender,instance,created,**kwargs):
    if created:
        print("Product added to cart successfully")


@receiver(post_delete,sender=cart)
def notify_cart_delete(sender,instance,**kwargs):
    print("Product deleted successfully!")

