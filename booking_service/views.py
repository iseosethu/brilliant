#Create your views here.

# booking_service/views.py
from django.shortcuts import render, redirect

def book_service(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service_type = request.POST.get('service_type')
        preferred_date = request.POST.get('preferred_date')
        preferred_time = request.POST.get('preferred_time')

        # You can log or store this data here

        return redirect('booking_thankyou')
    
    return render(request, 'booking_service/booking_form.html')


#from django.shortcuts import render, redirect
#from .forms import BookingForm

#def booking_view(request):
#    if request.method == 'POST':
#        form = BookingForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('booking_thankyou')
#    else:
#        form = BookingForm()
#    return render(request, 'booking_service/booking_form.html', {'form': form})

def booking_thankyou(request):
    return render(request, 'booking_service/thankyou.html')
