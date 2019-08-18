from django.shortcuts import render
from .models import Service

# Create your views here.


def services(request):

    services=Service.objects.all()

    context={

        'services':services,

    }
    return render(request ,'services.html',context)





