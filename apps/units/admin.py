from django.contrib import admin
from apps.units import models
# Register your models here.
admin.site.register(models.Unit)
# we want to see this model in the admin page, above code does this