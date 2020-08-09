from django.urls import path, include


urlpatterns = [
    path('', include('airplanes.api.urls')),
]