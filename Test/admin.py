from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import *

class BookAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Tester)
admin.site.register(Book, BookAdmin)
admin.site.register(Question)
