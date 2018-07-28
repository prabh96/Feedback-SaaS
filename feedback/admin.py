from django.contrib import admin

# Register your models here.
from .models import Url, Affective, Cognitive

admin.site.register(Url)
admin.site.register(Affective)
admin.site.register(Cognitive)