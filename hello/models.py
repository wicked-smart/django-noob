from django.db import models

# Create your models here.

class Userr(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"User {self.name} has email {self.email} as id"
    