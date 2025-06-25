from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from predictionserver import views

urlpatterns = [
    path('predictionserver/predict/', views.SensorPOST.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)