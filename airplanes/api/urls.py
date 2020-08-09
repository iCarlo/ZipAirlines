from django.urls import path
from .views import api_overview, airplane_list


urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('airplane-list/', airplane_list, name='airplane-list'),
]