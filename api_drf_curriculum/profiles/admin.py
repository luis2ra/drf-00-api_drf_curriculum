"""Profiles admin classes."""

# Django
from django.contrib import admin

# Models
from profiles.models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    """Plan admin."""

    list_display = ('id', 
        'name', 
        'type_plan',
        'image',
        'amount',
        'max_suscriptors',
        'is_selected')

    # list_display_links = ('pk', 'username', 'email',)

    # search_fields = (
    #     'email',
    #     'username',
    #     'first_name',
    #     'last_name',
    # )

    # list_filter = (
    #     'is_active',
    #     'is_staff',
    #     'date_joined',
    #     'modified',
    # )

    # readonly_fields = ('date_joined', 'modified',)