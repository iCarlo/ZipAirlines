from django.urls import path
from .views import api_overview, airplane_list, airplane_detail, airplane_add, airplane_update, airplane_delete


urlpatterns = [
    path('', api_overview, name='api-overview'),
    path('airplane-list/', airplane_list, name='airplane-list'),
    path('airplane-detail/<str:pk>/', airplane_detail, name='airplane-detail'),
    path('airplane-add/', airplane_add, name='airplane-add'),
    path('airplane-update/<str:pk>/', airplane_update, name='airplane-update'),
    path('airplane-delete/<str:pk>/', airplane_delete, name='airplane-delete'),
]