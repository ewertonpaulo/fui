from django.db import models

# Create your models here.
class King(models.Model):
    full_name = models.CharField(max_length = 50)
    rg = models.CharField(max_length = 20)
    cpf_cnpj = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    job = models.CharField(max_length = 50)
    andreess = models.CharField(max_length = 50)
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name