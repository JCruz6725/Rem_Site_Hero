
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from info_api.models import Person
from .serializers import PersonSerializer

@csrf_exempt
#@api_view(['GET', 'POST'])
def person_list(request):
    
    if (request.method == 'GET'):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif (request.method == 'POST'):
        data = JsonParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)