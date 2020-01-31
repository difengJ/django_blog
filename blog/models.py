from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Material(models.Model):
    """
    物料
    """
    material_name = models.CharField(max_length=40)
    date_added = models.DateTimeField(default=timezone.now)
    stock_price = models.DecimalField(max_digits=14,decimal_places=4)
    purchase_price = models.DecimalField(max_digits=14,decimal_places=4)
    author = models.ForeignKey(User,on_delete =models.CASCADE)

    def __str__(self):
        return self.material_name

    def  get_absolute_url(self):
        return reverse('material-detail', kwargs={'pk':self.pk})