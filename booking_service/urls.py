from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booking_view, name='book_service'),
    path('thankyou/', views.booking_thankyou, name='booking_thankyou'),
]
