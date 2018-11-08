from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=20)
    df = models.CharField(max_length=15)

    def __str__(self):
        return self.city + " " + self.df

class User_animal(models.Model):

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    type = models.CharField(max_length=6, default='Animal')
    address = models.OneToOneField(Address, related_name="address", on_delete=models.CASCADE, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='clients_photos/', default='clients_photos/default.jpg')



    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class User_wishes(models.Model):
    FREQUENCY_CHOICES = (
        ('1','1 vez por semana'),
        ('2','2 vezes por semana'),
        ('3','3 vezes por semana'),
        ('>3','Mais de 3 vezes')
    )
    TYPE_CHOICES = (
        ('C','Cultural'),
        ('F','Festas'),
        ('S','Shows'),
        ('E','Exposições')
    )
    TASTE_CHOICES = (
        ('S','Sertanejo'),
        ('F','Funk'),
        ('R','Rock'),
        ('O','Outros')
    )
    YN_CHOICES = (
        ('Y','Sim'),
        ('N','Não'),
    )
    PRICE_CHOICES = (
        ('free','Sim'),
        ('10~20','De R$10 até R$20'),
        ('20~30','De R$20 até R$30'),
        ('>30','Mais de R$30'),
    )
    user = models.ForeignKey(User_animal, blank=True, null=True, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=4, choices=FREQUENCY_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True)
    music_taste = models.CharField(max_length=2, choices=TASTE_CHOICES, blank=True, null=True)
    drink = models.CharField(max_length=2, choices=YN_CHOICES, blank=True, null=True)
    price = models.CharField(max_length=5, choices=PRICE_CHOICES, blank=True, null=True)
    distance = models.CharField(max_length=2, choices=YN_CHOICES, blank=True, null=True)
