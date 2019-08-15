from django.shortcuts import render
from services.models import Service
from departments.models import Department

# Create your views here.


def index(request):
    services=Service.objects.all()
    departments=Department.objects.all()
    context={

        'services':services,
        'departments':departments,
        
        
    }
    return render(request ,'index.html',context)


def about(request):
    context=[

    ]
    return render(request ,'about.html',)