from django.db import models

# Create your models here.
class Iteam(models.Model):
    name = models.CharField(max_leanght=250)
    is_bouth=models.BooleanField(default=False)
    added_at=models.DataTimeField(auto_now_add=True)