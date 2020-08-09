from django.urls import path, include


urlpatterns = [
    path('api/', include('airplanes.api.urls')),
]