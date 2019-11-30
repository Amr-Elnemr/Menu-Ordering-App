from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class users(models.Model):
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=255)
#     email = models.CharField(max_length=150)

class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=5, choices=(('pi', 'pizza'),('pa', 'pasta'),('sa', 'salad')))
    def __str__(self):
        return f"{self.id} - {self.name}"


class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete = models.CASCADE)
    status = models.CharField(max_length=10, choices=(('c', 'completed'),('p','pending')))
    def __str__(self):
        return f"{str(self.id)} - {User.objects.all().filter(id=int(self.user_id.id)).first().username}"


