from django.db import models


class Personal(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    personalID=models.CharField(max_length=15)

    def __str__(self):
        return self.name


