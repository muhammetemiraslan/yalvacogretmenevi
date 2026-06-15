from django.contrib import admin
from .models import Room, GalleryImage, Announcement, MenuItem, HistoryEvent, RoomImage

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

admin.site.register(Room, RoomAdmin)
admin.site.register(GalleryImage)
admin.site.register(Announcement)
admin.site.register(MenuItem)
admin.site.register(HistoryEvent)

from .models import Room, GalleryImage, Announcement, MenuItem, HistoryEvent, RoomImage, ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'is_read')
    list_filter = ('is_read',)

admin.site.register(ContactMessage, ContactMessageAdmin)

from .models import (
    Room, GalleryImage, Announcement, MenuItem,
    HistoryEvent, RoomImage, ContactMessage, HomePageContent
)

admin.site.register(HomePageContent)