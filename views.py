from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')
def single(request):
    return render(request, 'pages/single.html')
def register(request):
    return render(request, 'pages/register.html')
def login(request):
    return render(request, 'pages/login.html')
def contact(request):
    return render(request, 'pages/contact.html')
def blog3(request):
    return render(request, 'pages/blog3.html')
def blog2(request):
    return render(request, 'pages/blog2.html')
def blog1(request):
    return render(request, 'pages/blog1.html')
def about(request):
    return render(request, 'pages/about.html')
