from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Contact1

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def sendContact(request):
    if request.method == 'POST':
        contact = Contact1()
        contact.email = request.POST.get('email')
        contact.name = request.POST.get('name')
        contact.address = request.POST.get('address')
        contact.message = request.POST.get('message')
        contact.save()
        return HttpResponseRedirect('/')