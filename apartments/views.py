from django.shortcuts import render
from apartments.models import Apartment, Owner


def home_view(request):

    data = Apartment.objects.filter(activated=True)


    return render(request, 'apartments/home.html', {
        'data': data
    })


def detail_view(request, id):
    data = None
    data2 = None
    try:
        data = Apartment.objects.get(id=id)
        data2 = Owner.objects.get(id=id)
    except:
        pass

    return render(request, 'apartments/detail.html', {
        'data': data,
        'data2': data2
    })


