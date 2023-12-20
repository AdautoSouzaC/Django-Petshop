from django.contrib import admin
from base.models import Contato
from django.contrib import messages
# Register your models here.
@admin.action(description='Marcar formulário de contato como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulário de contato marcado como lido', messages.SUCCESS)


@admin.register(Contato)
class ContatoAdmim(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data', 'lido']
    search_fields = ['nome', 'email']
    list_filder = ['data', 'lido']
    actions = [marcar_como_lido]
