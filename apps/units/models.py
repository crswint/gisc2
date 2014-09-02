from django.db import models

# Create your models here.
class Unit(models.Model):
    """This model holds GPS units"""
    name = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    desc = models.CharField(max_length=280)

    def __str__(self):
        return "{}".format(self.name)