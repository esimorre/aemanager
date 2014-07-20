from django.contrib import admin
from autoentrepreneur.models import UserProfile, SalesLimit, Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    ordering = ['owner__username']

admin.site.register(UserProfile)

class SalesLimitAdmin(admin.ModelAdmin):
    save_as=True
admin.site.register(SalesLimit, SalesLimitAdmin)

admin.site.register(Subscription, SubscriptionAdmin)
