from django.contrib import admin
from .models import faculty,staff

# Register your models here.
admin.site.register(faculty)
admin.site.register(staff)
admin.site.site_header = 'Admin Dashboard'
