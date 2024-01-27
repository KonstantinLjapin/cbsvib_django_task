from django.contrib import admin
from .models import UserProfile, Organization, Event


@admin.register(UserProfile)
class CustomUser(admin.ModelAdmin):
    pass


@admin.register(Organization)
class CustomOrganization(admin.ModelAdmin):
    pass


@admin.register(Event)
class CustomOrganization(admin.ModelAdmin):
    pass
