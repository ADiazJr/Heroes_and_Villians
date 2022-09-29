from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import super_types

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super

@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        # sort_param = request.query_params.get('sort')

        supers = Super.objects.all()

        if type_param:
            supers = Super.objects.filter(super_type__type=type_param)
        # if sort_param:
        #     type = SuperType.objects.order_by(sort_param)
            
            serializer = SuperSerializer(supers, many=True)

        else:
            super_types = SuperType.objects.all()
            custom_response_dictionary = {}
            for type in super_types:

                supers = Super.objects.filter(super_type_id=type.id)
                super_serializer = SuperSerializer(supers, many=True)

                custom_response_dictionary[type.type] = {
                    "supers": super_serializer.data
                }
            return Response(custom_response_dictionary)

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