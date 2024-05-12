from asyncio.windows_events import NULL
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import Signal
from .models import *
from django.db.models import Q
from datetime import date
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response

# Create your views here.

def home(request):
    name = request.GET.get('name')
    catego=category_choices
    categories_value=[]
    for i in catego:
        for j in i:
            categories_value.append(j)
            break
    obj1=product.objects.all()
    if name==None:
        var1='none'
        var2='flex'
    else:
        var1='flex'
        var2='none'
    return render(request,'index.html',{'product':obj1,'Categories':categories_value,'uname':name,'var1':var1,'var2':var2})

def shop(request):
    main=product.objects.all()
    url = request.build_absolute_uri() #http://127.0.0.1:8000/shop/?name=mitesh04,category=Smartphone
    page = url.split('=')
    page2=page[1].split(',')
    if page[2] == "Smartphone":
        obj1=product.objects.filter(category="Smartphone")
    elif page[2] == 'SmartTv':
        obj1=product.objects.filter(category="SmartTv")
    elif page[2] == 'Laptop':
        obj1=product.objects.filter(category="Laptop")
    elif page[2] == 'Headphone':
        obj1=product.objects.filter(category="Headphone")
    elif page[2] == 'SmartWatch':
        obj1=product.objects.filter(category="SmartWatch")
    elif page[2] == 'Camera':
        obj1=product.objects.filter(category="Camera")
    elif page[2] == 'Speaker':
        obj1=product.objects.filter(category="Speaker")
    return render(request,'shop.html',{'specified_products':obj1,'main':main,'uname':page2[0]})

def product_detail(request):
    url = request.build_absolute_uri()
    urll=url.split('=')
    urll2=urll[1].split(',')
    item=product.objects.get(id=urll[2])
    return render(request,'detail.html',{'item':item,'uname':urll2[0],'id':urll[2]})

def mycart(request):
    
    url = request.build_absolute_uri()
    urll=url.split('=')
    #print(urll)
    try:
        if urll[1] == 'None':
            messages.error(request,'Please login or register to view your cart')
            return redirect('http://127.0.0.1:8000/login/')
        else:
            user = User.objects.get(username=urll[1])
            prod = cart.objects.filter(Q(user=user) & Q(pending=True)).order_by('-id')
            #print(prod)
            tprice=0
            for i in prod:
                if i!='':
                    quanttity=i.quantity
                    tprice=i.price+tprice
                    #print(tprice)
                    #print('quantiy : ',quanttity)
                    summary_price=tprice+100
                else:
                    messages.error(request,"No item added please add a item")
            
            return render(request,'cart.html',{'cart_item':prod,'uname':urll[1],'quanttity':quanttity,'summary_price':summary_price,'totall':tprice})
    except UnboundLocalError:
        messages.error(request,"No item added please add a item")
        return render(request,'cart.html',{'uname':urll[1]})

def checkout(request):

    url = request.build_absolute_uri()
    urll=url.split('=')

    if urll[1]!='None':
        user=User.objects.get(username=urll[1])
            
        userd=customer.objects.filter(user=user)

        try:
            prod = cart.objects.filter(Q(user=user) & Q(pending=True)).order_by('-id')

            tprice=0
            for i in prod:
                prodc=i.product
                quanttity=i.quantity
                tprice=i.price+tprice
                #print(tprice)
                #print('quantiy : ',quanttity)
                summary_price=tprice+100

            if request.method=='POST':
                check=request.POST['seladd']
                
                custd=customer.objects.filter(Q(user=user) & Q(add_count=check))

                custcard=cart.objects.filter(Q(user=user) & Q(pending=True)).order_by('-id')

                for c in custd:
                    name=c.name
                    num=c.phone
                    addr=c.address
                    co=c.country
                    st=c.state
                    ci=c.city
                    z=c.zipcode
                com_address=name+" "+str(num)+" "+addr+" "+co+" "+st+" "+ci+" "+str(z)


                for cc in custcard:

                    place=orderplaced.objects.create(user=user,product=cc.product,address_details=com_address,quantity=cc.quantity,total_amount=cc.price,ordered_date=date.today())

                    cartremove=cart.objects.filter(product=cc.product).delete()

                    url='http://127.0.0.1:8000/placed_order_details/?name={}'.format(urll[1])

                    return redirect(url,{'uname':urll[1]})

            return render(request,'checkout.html',{'uname':urll[1],'user_details':userd,'item_detail':prod,'summary_price':summary_price,'totall':tprice})
        except UnboundLocalError:
            messages.error(request,"No item added please add a item")
            return render(request,'cart.html',{'uname':urll[1]})

    else:
        messages.error(request,"Please login to checkout your items")
        return redirect('http://127.0.0.1:8000/login/')

def contact(request):
    return render(request,'contact.html',{})

def login(request):
    if request.method == 'POST':
        uname = request.POST['Username']
        password = request.POST['password']
        try :
            user = User.objects.get(username=uname)
            check = check_password(password,user.password)
            if check==True :
                url = 'http://127.0.0.1:8000/?name={}'.format(uname)
                return redirect(url)
            else :
                messages.error(request,'Invalid credentials!')
        except User.DoesNotExist:
            messages.error(request,'User is Not Here')
            return redirect('http://127.0.0.1:8000/login/')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        try:
            uname = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            password=make_password(password)
            conpass = request.POST['password2']
            myuser=User.objects.create(username=uname,email=email,password=password)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,'Registered successfully!')
            return redirect('http://127.0.0.1:8000/register/')
        except IntegrityError as error:
            if error=="UNIQUE constraint failed: auth_user.username":
                messages.error(request,'Username already exist!')
    return render(request,'register.html')

def loggedout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')

def add_to_cart(request):
    url = request.build_absolute_uri()
    urll=url.split('=')
    urll2=urll[1].split(',')
    if urll2[0]=='None':
        messages.error(request,'Please login or register to add items in your cart')
        return redirect('http://127.0.0.1:8000/login/')
    
    else:
        user=User.objects.get(username=urll2[0])
        prod=product.objects.get(id=urll[2])
        obj=cart.objects.create(user=user,product=prod,price=prod.discount_price)
        url = 'http://127.0.0.1:8000/cart/?name={}'.format(urll2[0])
        return redirect(url)

def cart_item_quantity(request):
    url = request.build_absolute_uri()
    urll=url.split('=')
    #print(urll)
    urll2=urll[1].split(',')
    #print(urll2)
    urll3=urll[2].split(',')
    user = User.objects.get(username=urll2[0])
    prod = cart.objects.filter(Q(user=user) & Q(id=urll[3]))
    for i in prod:
        quanttity=i.quantity
        #print(quanttity)
        total=i.price
        main_price=i.product.discount_price
    quanttity=quanttity+1
    #print(quanttity)
    totalprice=main_price+total
    quantinc=cart.objects.filter(Q(user=user) & Q(id=urll[3])).update(quantity=quanttity,price=totalprice)
    #print(quantinc)
    myurl='http://127.0.0.1:8000/cart/?name={}'.format(urll2[0])
    summary_total=totalprice+100
    #print(summary_total)
    return redirect(myurl,{'cart_item':prod,'summary_price':summary_total})

def dec_quantity(request):
    url = request.build_absolute_uri()
    urll=url.split('=')
    urll2=urll[1].split(',')
    user = User.objects.get(username=urll2[0])
    prod = cart.objects.filter(Q(user=user) & Q(id=urll[3])).order_by('-id')
    for i in prod:
        quanttity=i.quantity
        #print(quanttity)
        total=i.price
        main_price=i.product.discount_price
    
    if quanttity>1:
        quanttity=quanttity-1
        totalprice=total-main_price

    quantinc=cart.objects.filter(Q(user=user) & Q(id=urll[3])).update(quantity=quanttity,price=totalprice)
    #print(quantinc)

    myurl='http://127.0.0.1:8000/cart/?name={}'.format(urll2[0])

    summary_total=totalprice+100
    #print(summary_total)

    return redirect(myurl,{'cart_item':prod,'summary_price':summary_total})
    
def cart_item_delete(request):
    url = request.build_absolute_uri()
    urll=url.split('=')
    urll2=urll[1].split(',')
    user = User.objects.get(username=urll2[0])
    prod = cart.objects.filter(Q(user=user) & Q(pending=True)).order_by('-id')
    removee=cart.objects.filter(id=urll[2]).delete()
    myurl='http://127.0.0.1:8000/cart/?name={}'.format(urll2[0])
    return redirect(myurl,{'cart_item':prod})

def profile(request):
    
    url = request.build_absolute_uri()
    #print(url)
    page=url.split('/')
    #print(page)
    #print(len(page))

    if len(page)==5:
        userr=page[4].split('=')
        #print(userr)
        user=User.objects.get(username=userr[1])
    else:
        userr=page[5].split('=')
        myuser=userr[1].split(',')
        user=User.objects.get(username=myuser[0])

    countchoice=[]
    for c in country_choices:
        for j in c:
            countchoice.append(j)
            break
    statechoice=[]
    for s in state_choices:
        for j in s:
            statechoice.append(j)
            break

    if page[3]=='profile':
        var1='inline'
        var2='none'
        var3='none'
        
        if request.method=='POST':
            userr=request.POST['username']
            email=request.POST['email']
            fname=request.POST['fname']
            lname=request.POST['lname']
            updt=User.objects.filter(username=userr).update(email=email,first_name=fname,last_name=lname)

    elif page[3]=='manage_address':
        var1='none'
        var2='block'
        var3='none'
        #print(user)
        uuser=customer.objects.filter(user=user)
        namee=None
        count=0
        for i in uuser:
            count=count+1
            #print(count)
            addcount=i.add_count
            addcount=count
            chnge=customer.objects.filter(name=i.name).update(add_count=addcount)
            #print(addcount)
            namee = i.user

        if namee==None:
            var4='flex'
            var5='none'
            var6='none'
        else:
            var4='none'
            var5='flex'
            var6='none'
        
        if page[4]=='edit_address':
            var4='flex'
            var5='none'
            #print(">>>>>>>",userr[2])
            uuser=customer.objects.filter(Q(add_count=userr[2]) & Q(user=user))
            if request.method=='POST':
                fname=request.POST['fname']
                email=request.POST['email']
                mobile=request.POST['mobno']
                address=request.POST['address']
                country=request.POST['country']
                city=request.POST['city']
                state=request.POST['state']
                zip=request.POST['zip']

                updt=customer.objects.filter(user=user).update(name=fname,phone=mobile,email=email,address=address,country=country,state=state,city=city,zipcode=zip)
            return render(request,'profile.html',{'uname':user.username,'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5,'var6':var6,'country_choices':countchoice,'state_choices':statechoice,'address_details':uuser})
            
        elif page[4]=='delete_address':
            dlt=customer.objects.filter(add_count=userr[2]).delete()
            url="http://127.0.0.1:8000/manage_address/?name={}".format(myuser[0])
            return redirect(url,{'uname':user.username,'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5,'var6':var6,'country_choices':countchoice,'state_choices':statechoice,'address_details':uuser})
        elif page[4]=='add_address':
            var4='none'
            var5='none'
            var6='flex'
            if request.method=='POST':
                fname=request.POST['fname']
                email=request.POST['email']
                mobile=request.POST['mobno']
                address=request.POST['address']
                country=request.POST['country']
                city=request.POST['city']
                state=request.POST['state']
                zip=request.POST['zip']

                updt=customer.objects.create(user=user,name=fname,phone=mobile,email=email,address=address,country=country,state=state,city=city,zipcode=zip)
                return render(request,'profile.html',{'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5,'var6':var6,'uname':user.username,'country_choices':countchoice,'state_choices':statechoice})
        else:
            pass
        return render(request,'profile.html',{'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5,'var6':var6,'uname':user.username,'address':uuser,'country_choices':countchoice,'state_choices':statechoice})
    else:
        var1='none'
        var2='none'
        var3='inline'

        ordered_details=orderplaced.objects.filter(user=user)

        return render(request,'profile.html',{'var1':var1,'var2':var2,'var3':var3,'uname':user.username,'od':ordered_details})

    return render(request,'profile.html',{'var1':var1,'var2':var2,'var3':var3,'uname':user.username,'country_choices':countchoice,'state_choices':statechoice,'u':user})

def placed_order_details(request):
    url = request.build_absolute_uri()
    urll=url.split('=')

    user=User.objects.get(username=urll[1])

    ordered_details=orderplaced.objects.filter(Q(user=user) & Q(ordered_date=date.today()))

    return render(request,'placed_order_details.html',{'od':ordered_details,'uname':urll[1]})


@api_view(['GET'])
def get_products(request,pk=None):
    if request.method=='GET':
        id=pk
        if id is not None:
            stu=product.objects.get(id=id)
            serializer=productserializer(stu)
            return Response(serializer.data)

        stu=product.objects.all()
        serializer=productserializer(stu,many=True)
        return Response(serializer.data)