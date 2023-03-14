from django.db import models

# Create your models here.

class EmailVal(models.Model):
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)