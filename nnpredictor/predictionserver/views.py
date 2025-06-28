from .serializers import SensorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import make_prediction
from django.conf import settings
from drf_spectacular.utils import extend_schema


def is_valid(data):
    """Валидация спрогнозированных данных. Проверяется, что: \n
    - Списки всех характеристик имеют одинаковый размер, равный settings.EXIT_LENGTH;
    - Все характеристики, хранящиеся в settings.FIELDS, присутствуют в ответе.
    """
    for field in settings.FIELDS:
        if len(data[field]) != settings.EXIT_LENGTH:
            return False
        if field not in data:
            return False
    return True
        
# Create your views here.
class SensorPOST(APIView):
    """View для создания нового батча данных и отправки сгенерированных на его основе данных клиенту
    """

    @extend_schema(request=SensorSerializer, responses={201: SensorSerializer})
    def post(self, request, format=None):
        """По POST-запросу отправляются данные. В нём: \n
        - Сериализатор анализитует данные на соответсвие паттерну;
        - По переданным данным выполняется прогнозирование;
        - Выполняется сверка соответствия формата прогнозированных данных требуемой схеме;
        - Если всё прошло успешно, то возвращается ответ с прогнозом.\n
        Возможные ответы: \n
        - 200 - данные приняты и обработаны;
        - 400 - переданные данные не прошли проверку на соответсвие паттерну;
        - 500 - спрогнозированные данные не прошли проверку на соответсвие паттерну;
        """
        serializer = SensorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        predictedData = make_prediction(serializer.data)

        if not is_valid(predictedData):
            return Response({"error": "Internal processing error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(predictedData, status=status.HTTP_200_OK)