from django.urls import path
from .views import api_overview, airplane_list, airplane_detail


urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('airplane-list/', airplane_list, name='airplane-list'),
    path('airplane-detail/<str:pk>/', airplane_detail, name='airplane-detail'),
]