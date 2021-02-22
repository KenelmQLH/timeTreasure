from django.contrib import admin


# Register your models here.
from app import models
admin.site.register(models.Users)
admin.site.register(models.Projects)
admin.site.register(models.Records)
admin.site.register(models.Subprojects)
