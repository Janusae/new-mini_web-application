from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView, ListView, DetailView

from .models import Db_addForm
from .form import Add_Data_Form
from contact.models import Db_contact

class AddDataView(CreateView):
    template_name = "products/add_products.html"
    model = Db_addForm
    form_class = Add_Data_Form
    context_object_name = "data"
    success_url = "list_products"
class listProducttView(ListView):
    template_name = "products/products.html"
    model = Db_addForm
    context_object_name = "data"
class Detail(DetailView):
    template_name = "products/detail.html"
    model = Db_addForm
    context_object_name = "data"
    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context["forms"] = Db_contact.objects.all()
        context["number"] = Db_contact.objects.count()

        return context
