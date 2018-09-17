from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class King(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    full_name = models.CharField(max_length = 50, null = True )
    rg = models.CharField(max_length = 20, null = True)
    cpf_cnpj = models.CharField(max_length = 20, null = True)
    phone = models.CharField(max_length = 20, null = True)
    job = models.CharField(max_length = 50, null = True)
    andress = models.CharField(max_length = 50, null = True)
    since = models.DateTimeField(auto_now_add=True, null = True)
    photo = models.ImageField(upload_to = 'clients_photos', null = True)


    def __str__(self):
        return self.full_name