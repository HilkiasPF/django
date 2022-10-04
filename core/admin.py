from django.contrib import admin
from .models import ContatoModel

@admin.register(ContatoModel)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo')