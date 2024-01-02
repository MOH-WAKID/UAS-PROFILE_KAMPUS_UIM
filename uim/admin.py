from django.contrib import admin
from uim.models import SejarahKampus, VisiMisi
# Register your models here.

class SejarahKampusAdmin(admin.ModelAdmin):
    list_display = ['nama', 'tanggal_berdiri',]
    search_fields = ['nama', 'tanggal_berdiri',]

admin.site.register(SejarahKampus, SejarahKampusAdmin)
admin.site.register(VisiMisi)
