from django.contrib import admin
from .models import Event,EventImage

# Register your models here.
class EventImageAdmin(admin.StackedInline):
    model = EventImage

@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    inlines = [EventImageAdmin]

    class Meta:
       model = Event

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    pass