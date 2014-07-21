from django.contrib import admin
from autoentrepreneur.models import UserProfile, SalesLimit, Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    ordering = ['owner__username']

admin.site.register(UserProfile)

class SalesLimitAdmin(admin.ModelAdmin):
    list_display = ('year', 'activity', 'limit', 'limit2')
    list_filter = ('year', 'activity')
    save_as=True
admin.site.register(SalesLimit, SalesLimitAdmin)

admin.site.register(Subscription, SubscriptionAdmin)
