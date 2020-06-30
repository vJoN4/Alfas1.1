from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class usuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Extras', {
                'fields' : (
                    'foto',
                )
            }),
    )
admin.site.register(User, usuarioAdmin)