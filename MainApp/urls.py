from django.urls import path
from MainApp import views
urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('updatecategory/<int:updateid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:deleid>/', views.deletecategory, name="deletecategory"),
    path('editcategory/<int:editid>/', views.editcategory, name="editcategory"),
    path('addvehicles/', views.addvehicles, name="addvehicles"),
    path('displayvehicles/', views.displayvehicles, name="displayvehicles"),
    path('savevehicle/', views.savevehicle, name="savevehicle"),
    path('editvehicle/<int:editid>/', views.editvehicle, name="editvehicle"),
    path('updatevehicle/<int:updateid>/', views.updatevehicle, name="updatevehicle"),
    path('deletevehicle/<int:deleid>/', views.deletevehicle, name="deletevehicle"),

]