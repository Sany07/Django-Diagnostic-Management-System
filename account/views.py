from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages , auth
from .forms import EmailForm
from django.core.mail import EmailMessage
from django.conf import settings

def register(request):

    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        phone= request.POST['phone']
        user_name= request.POST['user_name']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        
        if password1 == password2:

            if User.objects.filter(username = user_name).exists():
                messages.error(request,' User name already taken')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,' Email already used')
                    return redirect('register')

                else:

                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,password=password1,  email=email )
                    
                    user.save()

                    messages.success(request,' You can log in')
                    return redirect('login')

        else:


            messages.error(request,' Password do not match')
            return redirect('contact')

    return render(request,'register.html')





def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username = username, password= password)
    
        if user is not None:

            auth.login(request,user)
            messages.success(request,' Login Success')
            return redirect('dashboard')
        else:
            messages.success(request,' Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

@login_required
def dashboard(request):

    return render(request,'dashboard.html')


@staff_member_required
def send_email(request):
    if request.method != 'POST':
        form = EmailForm()
        return render(request,'Email.html', {'email_form': form})
	
    form = EmailForm(request.POST, request.FILES)	
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        attach = request.FILES['attach']
        try:
            mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
            mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            return render(request,'email.html', {'message': 'Sent email to %s'%email})

        except (ValueError, TypeError, AttributeError, KeyError):

            context
            
    return render(request,'email.html')	
