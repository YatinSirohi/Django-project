from django.shortcuts import render
from django.http import HttpResponse
from .models import store, tub
# Create your views here.

def store_view(request):
    stores = store.objects.all()
    return render(request, 'store.html', {'stores':stores})

def tub_view(request):
    tubs = tub.objects.all()
    return render(request, 'tub.html', {'tubs':tubs})

def details(request, store_id):
    stores = store.objects.get(id= store_id)
    tubs = stores.tubs.all()
    return render(request, 'details.html', {'stores' : stores,'tubs':tubs})
