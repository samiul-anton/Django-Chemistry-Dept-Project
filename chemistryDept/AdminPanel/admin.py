from django.contrib import admin
from .models import faculty

# Register your models here.
admin.site.register(faculty)
admin.site.site_header = 'Admin Dashboard'
