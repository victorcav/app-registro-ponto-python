from django.contrib import admin
from .models import Funcionario, ColetaFaces, Treinamento

class ColetaFacesInline(admin.StackedInline):
    model = ColetaFaces
    extra = 0

class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    inlines = (ColetaFacesInline,)

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Treinamento)

# Register your models here.
