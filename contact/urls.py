from django.urls import path
from . import views
urlpatterns = [
    path("" , views.ShowFormView.as_view() , name = "contact")
]