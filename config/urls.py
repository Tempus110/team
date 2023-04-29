from django.contrib import admin
from django.urls import path, include
from hongapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hong/", include("hongapp.urls")),
    #path("", views.main),
    
]
