
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Airplanes

from .serializers import AirplanesSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/airplane-list/',
        'Detail View': '/airplane-detail/<str:pk>',
        'Create': '/airplane-add/',
        'Update': '/airplane-update/<str:pk>',
        'Delete': '/airplane-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def airplane_list(request):
    airplanes = Airplanes.objects.all()
    serializer = AirplanesSerializer(airplanes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def airplane_detail(request, pk):
    airplanes = Airplanes.objects.get(id=pk)
    serializer = AirplanesSerializer(airplanes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def airplane_add(request):
    serializer = AirplanesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)