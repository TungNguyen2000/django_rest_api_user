from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.name