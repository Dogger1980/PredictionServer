from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from predictionserver import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('predictionserver/predict/', views.SensorPOST.as_view()),
    path('predictionserver/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('predictionserver/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns = format_suffix_patterns(urlpatterns)