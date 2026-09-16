# Register your models here.
from django.contrib import admin

from .models import Hotel
# registering the model in the admin side 

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):

    list_display = (
        'hotel_name',
        'guest_name',
        'email',
        'room_number',
        'room_type',
        'price_per_night',
        'is_available',
    )

    search_fields = (
        'hotel_name',
        'guest_name',
        'email',
    )

    list_filter = (
        'room_type',
        'is_available',
        'country',
    )
