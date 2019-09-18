from django.shortcuts import render
from . models import Department,Doctor
from django.shortcuts import get_object_or_404
# Create your views here.

def About(request):

    departments=Department.objects.all()
    doctor=Doctor.objects.all()

    context={

        'doctors':doctor
    }

    return render(request,'about.html',context)
    
def doc_detail(request, id):

    doc_detail=Doctor.objects.get(pk=id)
    
    context={

        
        'doc':doc_detail
    }

    return render(request,'doc_detail.html',context)

def detail(request, id):

    dep_detail=Department.objects.get(pk=id)
    
    context={

        'dep_detail':dep_detail
    }

    return render(request,'detail.html',context)





