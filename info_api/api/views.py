from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from info_api.models import Person
from .serializers import PersonSerializer

@api_view(['GET', 'POST'])
def person_list(request):
    
    if (request.method == 'GET'):
        person = Person.objests.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)