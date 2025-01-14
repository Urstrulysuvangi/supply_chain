from django.shortcuts import render
from geopy.geocoders import Nominatim
from .forms import SellerForm, ReceiverForm
from geopy.distance import geodesic

geocoder = Nominatim(user_agent = 'Supply chain')

def calculate_distance_view(request):
    seller_form = SellerForm(request.POST or None)
    receiver_form = ReceiverForm((request.POST or None))

    if seller_form.is_valid():
        seller_form.save()
        seller_pincode = seller_form.cleaned_data.get('pincode')
        seller_pincode = geocoder(seller_pincode)

        # destination coordinates
        d_latA = seller_pincode.latitude
        d_lonA = seller_pincode.longitude
        pointA = (d_latA, d_lonA)
        
    
    if receiver_form.is_valid():
        receiver_form.save()
        pincode = receiver_form.cleaned_data.get('pincode')
        destination = geocoder(pincode)

        # destination coordinates
        d_latB = destination.latitude
        d_lonB = destination.longitude
        pointB = (d_latB, d_lonB)

    # distance calculation
    distance = round(geodesic(pointA, pointB).km, 2)
    
    context = {
    'distance' : distance,
    'seller_form': seller_form,
    'receiver_form': receiver_form,
    }
    print(distance)
    return render(request, 'main.html', context)

''' Right now there is no template for delivery page 
    When it is available we need to add it to the render path
'''