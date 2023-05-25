from django.contrib import admin
from vehical_managementapp.models import info
# Register your models here.
class infoadmin(admin.ModelAdmin):
    list_display=['num','vtype','vmodel','vdesc']
admin.site.register(info,infoadmin)
admin.site.site_header="Vehical Management"