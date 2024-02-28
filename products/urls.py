from django.urls import path
from . import views
urlpatterns = [
    path("add" , views.AddDataView.as_view() , name= "add_products"),
    path("list_products" , views.listProducttView.as_view() , name = "list_products"),
    path("<int:pk>" , views.Detail.as_view() , name = "detail")
]