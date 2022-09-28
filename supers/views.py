from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        super_types = Super.objects.all()
        serializer = SuperSerializer(super_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
            serializer =SuperSerializer(supers)
            return Response(serializer.data)
    elif request.method == 'PUT':
            serializer = SuperSerializer(supers, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
            supers.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)