from django.shortcuts import render
from django.http import HttpResponse
from .models import Personal


def index(request):
    if request.method == "POST":
        personal=Personal()
        name=request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        personalID = request.POST.get('personalID')
        personal.name=name
        personal.phone = phone
        personal.address = address
        personal.personalID = personalID
        personal.save()
        return HttpResponse("<h2>Спасибо</h2>")
    return render(request, 'index.html')
