from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    # return HttpResponse("Hello world~!")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("about page!성공했구나")
    return render(request,'about.html')

