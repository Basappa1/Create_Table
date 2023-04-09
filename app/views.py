from django.shortcuts import render


# Create your views here.
from app.models import *

def Topic_display(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'Topic_display.html',d)
