from django.shortcuts import render
from .models import Db_contact
from .form import Form
# Create your views here.
from django.views.generic import FormView, CreateView


class ShowFormView(CreateView):
    template_name = "contact/form.html"
    form_class = Form
    model = Db_contact
    context_object_name = "data"
    success_url = "/products/list_products"

