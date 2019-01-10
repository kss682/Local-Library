from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    return render(request,'base.html',{})

def contacts(request):
    return render(request,"contacts.html",{})

def about(request):
    return render(request,"about.html",{})

class ContactView(TemplateView):
    template_name = 'contacts.html'
