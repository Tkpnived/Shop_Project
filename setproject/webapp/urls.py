from django.urls import path
from webapp import views


urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("about/",views.about,name="about"),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('shop/<itemspro>/',views.shop,name='shop'),
    path('single/<int:dataid>',views.single,name='single'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userlogindetail/',views.userlogindetail,name='userlogindetail'),
    path('loginusers/',views.loginusers,name='loginusers'),
    path('contactdetails/',views.contactdetails,name='contactdetails'),
    path('conlogout/',views.conlogout,name='conlogout'),
    path('addcart/<int:dataid>',views.addcart,name='addcart'),
    path('showcart/',views.showcart,name='showcart'),
    path('deletecart/<int:dataid>',views.deletecart,name='deletecart'),



]
