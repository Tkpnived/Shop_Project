from django.urls import path
from setapp import views


urlpatterns = [
    path("set/",views.set,name="set"),
    path("addset/",views.addset,name="addset"),
    path('setaddfun/',views.setaddfun,name="setaddfun"),
    path('showset/',views.showset,name="showset"),
    path('editset/<int:dataid>',views.editset,name="editset"),
    path("update_set/<int:dataid>",views.update_set,name="update_set"),
    path("deleteset/<int:dataid>",views.deleteset,name="deleteset"),

    path("newproduct/",views.newproduct,name="newproduct"),
    path("addpro/",views.addpro,name="addpro"),
    path("showpro/",views.showpro,name="showpro"),
    path("editpro/<int:dataid>",views.editpro,name="editpro"),
    path("update_pro/<int:dataid>",views.update_pro,name="update_pro"),
    path("deletepro/<int:dataid>",views.deletepro,name="deletepro"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("adminlogin/",views.adminlogin,name="adminlogin"),
    path("adminlogout/",views.adminlogout,name="adminlogout"),
    path('showcontact/',views.showcontact,name='showcontact'),
    path('deletecontact/<int:dataid>',views.deletecontact,name='deletecontact'),
    path('cartdb',views.cartdb,name='cartdb')
    ]


