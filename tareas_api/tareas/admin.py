from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'hecho', 'created_at')
    list_filter = ('hecho',)
    search_fields = ('titulo',)
