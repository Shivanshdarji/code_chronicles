from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=50)

def __str__(self):
    return self.name

class UserMst(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    ContactNo=models.CharField(max_length=15)

    Username=models.CharField(max_length=40)

    Password=models.CharField(max_length=10)


class Leaderboard(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.username}: {self.score}"
