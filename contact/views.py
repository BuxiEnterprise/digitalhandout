from django.shortcuts import render,HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.

def init(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, '/contact/contact.html',{'posts':post})