from django.contrib import admin
from .models import faculty,staff,research_by_area

# Register your models here.
admin.site.register(faculty)
admin.site.register(staff)
admin.site.register(research_by_area)
admin.site.site_header = 'Admin Dashboard'
