from django.urls import path
from .views import *
urlpatterns = [
    path('', bookingpage, name="bookingpage"),
    path('dashboard/', dashboard, name="adminpage"),
    path('dashboard/search/', search_bookings, name='search_bookings'),
    path('download-all-bookings/', download_all_bookings, name='download_all_bookings'),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('success/', bookingsuccess, name="bookingsuccess"),
    path('success/download_receipt/<str:booking_code>/', download_receipt, name="download_receipt"),
    path('booking/delete/<int:booking_id>/', delete_booking, name="delete_booking"),
]
