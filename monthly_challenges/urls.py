from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def default_view(request):
    return HttpResponse("Welcome to My Site!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("challenge/", include("challenges.urls")),
    path("", default_view),  # Default view for the root path
]
