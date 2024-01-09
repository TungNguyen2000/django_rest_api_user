from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)
    email = models.EmailField(max_length=254, default='aaa@gmail.com')

    def __str__(self):
        return self.name