from django.contrib import admin

from . import models

models = [models.Post, models.List]
admin.site.register(models)
