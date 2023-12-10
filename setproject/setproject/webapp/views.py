from django.shortcuts import render, redirect
from setapp.models import setdb, prodb
from webapp.models import logindb,contactdb, cart
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def homepage(request):
    data=setdb.objects.all()
    return render(request,"web.html",{'data':data})
def about(request):
    data = setdb.objects.all()

    return render(request,"about.html",{'data':data})
def contact(request):
    data = setdb.objects.all()

    return render(request,"contact.html",{'data':data})
def shop(request,itemspro):
    data = setdb.objects.all()
    products=prodb.objects.filter(CategoryName=itemspro)
    return render(request,"shop.html",{'data':data,'products':products})

def single(request,dataid):
    data = setdb.objects.all()
    products=prodb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{"data":data,'products':products})
def userlogin(request):
    return render(request,'userlogin.html')
def userlogindetail(request):
    if request.method == "POST":
        n = request.POST.get("username")
        e = request.POST.get("email")
        p = request.POST.get("password")
        c = request.POST.get("confirm_password")


        obj = logindb(username=n, email=e, password=p, confirm_password=c)
        obj.save()

    return redirect(userlogin)
def loginusers(request):
    if request.method=='POST':
        username_r=request.POST.get('username')
        password_r = request.POST.get('password')
        if logindb.objects.filter(username=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password'] = password_r

            return redirect(homepage)
        else:
            return redirect(userlogin)
    return redirect(userlogin)

def contactdetails(request):
    if request.method == "POST":
        n = request.POST.get("yourname")
        e = request.POST.get("youremail")
        s = request.POST.get("subject")
        m = request.POST.get("message")


        obj = contactdb(yourname=n, youremail=e, subject=s, message=m)
        obj.save()
    return redirect(contact)
def conlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userlogin)


def addcart(request,dataid):
    if request.method == "POST":

        P = request.POST.get("productprice")
        Pr = request.POST.get("totalprice")
        Q = request.POST.get("Qty")
        s = request.POST.get("singleprice")
        IM = request.FILES["Images"]
        obj = cart(product=P, price=Pr, Qty=Q,singleprice=s,Images=IM)
        obj.save()
        messages.success(request, "Added to Cart Successfully")

        return redirect(showcart)
def showcart(request):
    pro = cart.objects.all()

    return render(request,"carts.html",{'pro':pro})
def deletecart(request, dataid):
    data=cart.objects.filter(id=dataid)
    data.delete()
    return redirect(showcart)

