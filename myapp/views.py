from django.shortcuts import render,redirect
from .models import project,certificate

def display(request):
    p = project.objects.all()
    c = certificate.objects.all()
    return render(request,'portfolio.html',{'p':p,'c':c})