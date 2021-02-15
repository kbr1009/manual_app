from django.contrib import admin
from .models import Section, Job, Item, Method, Procedure



myModels = [Section, Job, Item, Method, Procedure]
admin.site.register(myModels)

