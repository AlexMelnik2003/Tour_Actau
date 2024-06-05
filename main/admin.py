from django.contrib import admin
from django.contrib import admin
from .models import Destination, Tour, Book_list, TourImage, Booking, Category, TourVideo, Faq


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1


class TourVideoInline(admin.TabularInline):
    model = TourVideo
    extra = 1


class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]


admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Book_list)
admin.site.register(TourImage)
admin.site.register(TourVideo)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Faq)
