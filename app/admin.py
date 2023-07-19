from django.contrib import admin
from app.models import Vaga

class ListandoVaga(admin.ModelAdmin):
    list_display = ("id", "cargo_vaga", "faixa_salarial", "escolaridade_vaga", "publicada", )
    list_display_links = ("id", "cargo_vaga",)
    search_fields = ("cargo_vaga",)
    list_filter = ("escolaridade_vaga", "usuario", )
    list_editable = ("publicada",)
    list_per_page = 10
    
admin.site.register(Vaga, ListandoVaga)
