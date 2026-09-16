# Create your models here.

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
# for validator we import MinValueValidator and MaxValueValidator from django.core.validators


class Hotel(models.Model):

    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Deluxe', 'Deluxe'),
        ('Suite', 'Suite'),
    ]

    hotel_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15, unique=True)

    room_number = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(500)
        ]
    )

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES
    )

    price_per_night = models.FloatField(
        validators=[
            MinValueValidator(500),
            MaxValueValidator(100000)
        ]
    )

    guest_name = models.CharField(max_length=100)

    guest_age = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    is_available = models.BooleanField(default=True)

    check_in_date = models.DateField(auto_now_add=True)

    check_out_date = models.DateField(
        null=True,
        blank=True
    )

    booking_date = models.DateField(auto_now_add=True)

    special_request = models.TextField(
        blank=True,
        null=True
    )

    country = models.CharField(
        max_length=50,
        default='India'
    )

    class Meta:
        ordering = ['guest_name']
        db_table = 'hotel_booking'
        verbose_name = 'Hotel Booking'
        verbose_name_plural = 'Hotel Bookings'

    def __str__(self):
        return self.guest_name

