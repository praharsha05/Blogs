import django.contrib.admin
from django.contrib import admin
from pro.models import blogs,drafts

# Register your models here.
admin.site.register(blogs)
admin.site.register(drafts)