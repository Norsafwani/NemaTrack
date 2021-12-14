from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from trackApp.models import Nema2

# @admin.register(Nema)
# class NemaAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Nema)
# class NemaAdmin(ImportExportModelAdmin):
#     pass

@admin.register(Nema2)
class Nema2Admin(ImportExportModelAdmin):
    list_display = ("id", "devui")
    pass

