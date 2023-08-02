from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('predict/',predict,name='predict'),
    path('my_predictions/',my_predictions,name='my_predictions'),
    path('prediction_view/<int:id>',prediction_view,name='prediction_view'),
]