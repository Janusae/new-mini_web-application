from django import forms
from .models import Db_addForm
class Add_Data_Form(forms.ModelForm):
    class Meta:
        model = Db_addForm
        fields = "__all__"
        widgets = {
            "title" : forms.TextInput(attrs={
                "placeholder" : "Enter title",
                "row" : 5
            }),
            "name": forms.TextInput(attrs={
                "placeholder": "Enter name"
            }),
            "description": forms.TextInput(attrs={
                "placeholder": "Enter description"
            }),
            "price": forms.TextInput(attrs={
                "placeholder": "Enter price"
            }),
        }
        labels = {
            "name" : "نام"
        }