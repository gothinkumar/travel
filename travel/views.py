from django.shortcuts import render

from .models import Travel

# Create your views here.


def home(request):
    obj = Travel.objects.all()
    return render(request, 'index.html',{'obj':obj})

