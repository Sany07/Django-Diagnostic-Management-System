from django.shortcuts import render
from departments.models import Doctor,Department

# Create your views here.
def contact(request):


    departments=Department.objects.all()
    doctor=Doctor.objects.all()
    context={

        'departments':departments,
        'doctors':doctor
    }

    return render(request ,'contact.html',context)   