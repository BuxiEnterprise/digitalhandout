from django.shortcuts import render,HttpResponse

# Create your views here.

def init(request):
    return render(request,'contact/contact.html',{'user:':'Leozinho'})