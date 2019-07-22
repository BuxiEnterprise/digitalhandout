from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.init,name="contact"),
    path('post/<int:pk>/',views.post_detail, name="post_detail")
]
