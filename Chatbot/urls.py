from django.urls import path
from .views import PredictCOPDView


urlpatterns = [
    path('predict-copd/', PredictCOPDView.as_view(), name='predict_copd')
]
