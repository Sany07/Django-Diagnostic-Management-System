from django.shortcuts import render
from .models import Service,Vision,Mission,Center

# Create your views here.


def services(request):

    services=Service.objects.all()
    vision=Vision.objects.all()
    mission=Mission.objects.all()
    center=Center.objects.all()
    context={

        'services':services,
        'vision':vision,
        'mission':mission,
        'center':center
    }
    return render(request ,'services.html',context)





