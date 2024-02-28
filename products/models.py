from django.db import models

# Create your models here.
class Db_addForm(models.Model):
    title = models.CharField(max_length=50 , verbose_name="سربرگ محصول")
    name = models.CharField(max_length=50 , verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت محصول")
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"