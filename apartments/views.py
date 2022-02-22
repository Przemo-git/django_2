from django.shortcuts import render
from apartments.models import Apartment, Owner


def home_view(request):

    data = Apartment.objects.filter(activated=True).order_by('-date')


    return render(request, 'apartments/home.html', {
        'data': data
    })


def detail_view(request, id):
    data = None
    data2 = ''
    try:
        data = Apartment.objects.get(id=id)
        data2 = Owner.objects.get(name=id)

    except:
        pass

    print(data2)

    return render(request, 'apartments/detail.html', {
        'data': data,
        'data2': data2
    })
