from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Champs affichés dans la liste des utilisateurs
    list_display = ('username', 'email', 'matricule', 'age', 'is_staff', 'is_active')
    # Champs cliquables dans l'interface admin
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    # Champs disponibles dans le formulaire d'édition dans l'admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('email', 'matricule', 'age')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    # Champs disponibles lors de la création d'un utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'matricule', 'age', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'email', 'matricule')  # Champs à rechercher
    ordering = ('username',)  # Ordre par défaut des utilisateurs

# Enregistrement du modèle CustomUser dans l'admin
admin.site.register(CustomUser, CustomUserAdmin)
