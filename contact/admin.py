from django.contrib import admin
from . import models
# Register your models here.
class ChangeAdmin(admin.ModelAdmin):
    list_display = ["name" , "date_of_send" , "readed_by_admin"]
    list_filter = ["readed_by_admin"]
admin.site.register(models.Db_contact , ChangeAdmin)