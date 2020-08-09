from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/airplane-list/',
        'Detail View': '/airplane-detail/<str:pk>',
        'Create': '/airplane-add/',
        'Update': '/airplane-update/<str:pk>',
        'Delete': '/airplane-delete/<str:pk>',
    }
    return Response(api_urls)