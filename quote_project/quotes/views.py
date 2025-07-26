from django.shortcuts import render,redirect
from . models import *


def home(request):
    return render(request, 'home.html')
def request_quote(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def services1(request):
    return render(request, 'services1.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def pricing(request):
    return render(request, 'pricing.html')
def blog(request):
    return render(request, 'blog.html')


def quote_success(request):
    if request.method == 'POST':
        # Extract data from POST request
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        date_time= request.POST.get("date_time")
        distance = request.POST.get("distance")
        freight_type = request.POST.get("freight_type")
        pickup_address = request.POST.get("pickup_address")
        delivery_address= request.POST.get("delivery_address")


        # Optionally, you can create a Contact instance and save it directly
        contact = QuoteRequest.objects.create(
            name= name,
            phone= phone,
            email= email,
            date_time= date_time,
            distance= distance,
            freight_type= freight_type,
            pickup_address= pickup_address,
            delivery_address= delivery_address

        )
        contact.save()
        return render(request,"quote_success.html")





