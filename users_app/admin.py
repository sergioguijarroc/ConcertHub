from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Cliente
    fieldsets = UserAdmin.fieldsets + (
        (
            "Campos adicionales",
            {
                "fields": (
                    "vip",
                    "saldo",
                )
            },
        ),
    )
    # Con esto te saldra al crear un nuevo usuario desde admin los campos
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Campos adicionales",
            {
                "fields": (
                    "vip",
                    "saldo",
                )
            },
        ),
    )


admin.site.register(Cliente, CustomUserAdmin)
