from django.contrib.auth.models import User
from django.db import models
from user.models import User_animal
from event.models import Event

# Create your models here.

class Rating(models.Model):
    user_rated = models.ForeignKey(User_animal, blank=True, null=True, on_delete=models.CASCADE)
    event_rated = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    user = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    note = models.IntegerField(blank=True, null=True)

    def __int__(self):
        return self.note
