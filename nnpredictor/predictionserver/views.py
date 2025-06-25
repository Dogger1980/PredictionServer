from .serializers import SensorSerializer
from .models import SensorData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import make_prediction
from django.conf import settings


def validate_data(data):
    for field in settings.FIELDS:
        if len(data[field]) != settings.EXIT_LENGTH:
            return False
        if field not in data:
            return False
    return True
        
# Create your views here.
class SensorPOST(APIView):
    "View для создания нового батча данных и отправки сгенерированных на его основе данных клиенту"
    def post(self, request, format=None):
        serializer = SensorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        predictedData = make_prediction(serializer.data)

        if not validate_data(predictedData):
            return Response({"error": "Internal processing error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(predictedData, status=status.HTTP_200_OK)