from django.contrib import admin
from .models import Section, Job, Item, Method, Procedure, Annotation



myModels = [Section, Job, Item, Method, Procedure, Annotation]
admin.site.register(myModels)

