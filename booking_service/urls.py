from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_service, name='booking_home'),
    path('book/', views.book_service, name='book_service'),
    path('thankyou/', views.booking_thankyou, name='booking_thankyou'),
     
]
