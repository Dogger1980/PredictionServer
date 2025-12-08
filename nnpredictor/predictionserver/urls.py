from django.http.response import HttpResponse
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from predictionserver import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def favicon(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('predictionserver/predict/', views.SensorPOST.as_view()),
    path('predictionserver/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('predictionserver/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('favicon.ico', favicon),
]

urlpatterns = format_suffix_patterns(urlpatterns)