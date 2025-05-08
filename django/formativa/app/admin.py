from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Professor,Ambiente,Disciplina
# Register your models here.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Novos campos',{'fields': ('categoria',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('categoria',)}),
    )

admin.site.register(Professor,UsuarioAdmin)
admin.site.register(Ambiente)
admin.site.register(Disciplina)