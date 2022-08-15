from django.contrib import admin
from .models import Userinfo
from peopleApp.models import faculty,staff,student
from researchApp.models import research_overview,research_by_direction,research_by_area
from resourceApp.models import labFacility,computing

# Register your models here.
admin.site.register(faculty)
admin.site.register(staff)
admin.site.register(student)
admin.site.register(research_overview)
admin.site.register(research_by_area)
admin.site.register(Userinfo)
admin.site.register(labFacility)
admin.site.register(computing)
admin.site.register(research_by_direction)
admin.site.site_header = 'Admin Dashboard'
