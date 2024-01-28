from django.contrib import admin
from .models import UserProfile, Organization, Event


@admin.register(UserProfile)
class CustomUser(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'password', 'phone')
    list_filter = ('id', 'email', 'username', 'password', 'phone')


@admin.register(Organization)
class CustomOrganization(admin.ModelAdmin):
    #list_display = ("title", "description", "address", "postcode")
    #list_filter = ("title", "description", "address", "postcode")
    pass


@admin.register(Event)
class CustomEvent(admin.ModelAdmin):
    #list_display = ("title", "description", "organizations", "image", "date")
    #list_filter = ("title", "description", "organizations", "image", "date")
    pass
