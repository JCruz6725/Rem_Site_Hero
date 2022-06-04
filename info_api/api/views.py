
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



from info_api.models import Person
from .serializers import PersonSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
class person_v(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def person_list(request):

        if (request.method == 'GET'):
            person = Person.objects.all()
            serializer = PersonSerializer(person, many=True)
            return Response(serializer.data[0])

        elif (request.method == 'POST'):
            #data = JsonParser().parse(request)
            serializer = PersonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)