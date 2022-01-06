from django.db import models

# Create your models here.


class info_one(models.Model):
    name = models.CharField(max_length=20)
    roll = models.CharField(max_length=20)

    def __str__(self):
        return self.name + self.roll

class info_two(models.Model):
    name = models.CharField(max_length=20)
    roll = models.CharField(max_length=20)

    def __str__(self):
        return self.name + self.roll
