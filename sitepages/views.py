from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'sitepages/home.html')

def contact(request):
    return render(request,'sitepages/contact.html')
