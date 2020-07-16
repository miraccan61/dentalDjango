from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import AppoitmentForm,ContactForm
from django.urls import reverse_lazy

def home(request):
    return render(request,'home.html')
    

def appointment(request):
    if request.method == 'POST':
        forms = AppoitmentForm(request.POST or None)
        if forms.is_valid():      
            forms.save()
            return redirect('home')
    else:
        form = AppoitmentForm()
        return render(request, 'appointment.html', {'form':form})

def contact(request):
    if request.method == 'POST':
        forms = ContactForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        form=ContactForm()
        return render(request, 'contact.html',{'form':form})


def services(request):
    return render(request,'_service/service.html')

def pricing(request):
    return render(request,'prices/price.html')

def about(request):
    return render(request,'about/about.html')

