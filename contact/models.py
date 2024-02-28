from django.db import models

# Create your models here.
class Db_contact(models.Model):
    name = models.CharField(max_length=50 , verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    date_of_send = models.DateField(null=True , verbose_name="تاریخ ارسال",auto_now_add=True )
    response_by_admin = models.TextField(verbose_name="جواب ادمین",null=True , blank=True)
    readed_by_admin = models.BooleanField(verbose_name="خوانده شده توسط ادمین",default=False , null=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "فرم"
        verbose_name_plural = "فرم ها"
