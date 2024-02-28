from django import forms

from .models import Db_contact


class Form(forms.ModelForm):
    class Meta:
        model = Db_contact
        fields = "__all__"
        exclude = ["response_by_admin" , "readed_by_admin" , "date_of_send"]
        widgets = {
            "name" : forms.TextInput(attrs={
                "placeholder" : "Enter your name"
            }),
            "email": forms.TextInput(attrs={
                "placeholder": "Enter your email"
            }),
            "message": forms.TextInput(attrs={
                "placeholder": "Enter your message"
            }),
        }
        error_messages = {
            "required" : {
                "name" : "You must enter your name",
                "email" : "You must enter your email",
                "message" : "You must enter your message",
            }
        }
        labels = {
            "name" : "نام کاربری",
            "email" : "ایمیل",
            "message" : "پیام"
        }