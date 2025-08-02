# Create your views here.
from django.shortcuts import render, redirect
from .forms import BookingForm

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_thankyou')
    else:
        form = BookingForm()
    return render(request, 'booking_service/booking_form.html', {'form': form})

def booking_thankyou(request):
    return render(request, 'booking_service/thankyou.html')
