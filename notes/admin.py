from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . import models
# Register your models here.

class NotesAdmin(ModelAdmin):
    list_display = ('notes_id', 'title', 'pdf')
    list_display_links = ('notes_id',)
    search_fields = ('notes_id', 'title', 'pdf')
    list_editable = ('title',)
    list_max_show_all = 100


admin.site.register(models.Notes, NotesAdmin)
