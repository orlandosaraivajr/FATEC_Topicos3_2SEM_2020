from django.contrib import admin
from .models import FeriadoModel
from datetime import date

# admin.site.register(FeriadoModel)

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome','dia','mes','modificado_em','modificado_esse_ano')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome','dia','mes')
    list_filter = ('modificado_em','nome')

    def modificado_esse_ano(self, obj):
        hoje = date.today()
        return obj.modificado_em.year == hoje.year

    modificado_esse_ano.short_description = "Registrado este ano? "
    modificado_esse_ano.boolean = True

admin.site.register(FeriadoModel, FeriadoModelAdmin)