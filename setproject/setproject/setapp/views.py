import django
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from setapp.models import setdb, prodb
from webapp.models import contactdb, cart
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError




# Create your views here.

def set(request):
    return render(request, "index.html")
def addset(request):
    return render(request, "addset.html")

def setaddfun(request):

    if request.method == "POST":
        c = request.POST.get("categoryname")
        d = request.POST.get("description")


        IM = request.FILES["Image"]
        obj = setdb(CategoryName=c, Description=d,Image=IM)
        obj.save()
        messages.success(request, "added Successfully")
    return redirect(addset)

def showset(request):
    data=setdb.objects.all()
    return render(request, "displaytable.html", {"data": data})



def editset(request, dataid):
    data = setdb.objects.get(id=dataid)
    print(data)
    return render(request, "edit.html", {"data":data})

def update_set(request, dataid):
    if request.method=="POST":
        c = request.POST.get("CategoryName")
        d = request.POST.get("Description")


        try:
            IM=request.FILES['Image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=setdb.objects.get(id=dataid).Image

        setdb.objects.filter(id=dataid).update(CategoryName=c, Description=d,Image=file)
    return redirect(showset)
def deleteset(request, dataid):
    data=setdb.objects.filter(id=dataid)
    data.delete()
    return redirect(showset)


def newproduct(request):
    data = setdb.objects.all()
    return render(request, "addproduct.html",{"data":data})
def addpro(request):

    if request.method == "POST":

        c = request.POST.get("CategoryName")
        n = request.POST.get("Name")
        p = request.POST.get("Price")
        d = request.POST.get("Description")


        IM = request.FILES["Image"]
        obj = prodb(CategoryName=c,Name=n,Price=p, Description=d,Image=IM)
        obj.save()
        messages.success(request, "added Successfully")
        return redirect(newproduct)
def showpro(request):
    data=prodb.objects.all()
    return render(request, "displayprotable.html", {"data": data})
def editpro(request, dataid):
    data = prodb.objects.get(id=dataid)
    cat_data = setdb.objects.all()

    return render(request, "proedit.html", {"data":data,'cat_data':cat_data})

def update_pro(request, dataid):
    if request.method=="POST":
        c = request.POST.get("CategoryName")
        n = request.POST.get("Name")
        p = request.POST.get("Price")
        d = request.POST.get("Description")


        try:
            IM=request.FILES['Image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=prodb.objects.get(id=dataid).Image

        prodb.objects.filter(id=dataid).update(CategoryName=c,Name=n,Price=p, Description=d,Image=file)
    return redirect(showpro)


def deletepro(request, dataid):
    data=prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(showpro)
def loginpage(request):
    return render(request, "userlogin.html")


def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(set)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def showcontact(request):
    data=contactdb.objects.all()
    return render(request, "contact_table.html", {"data": data})
def deletecontact(request, dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(showcontact)
def cartdb(request):
    data = cart.objects.all()
    return render(request, "cart.html",{"data":data})
