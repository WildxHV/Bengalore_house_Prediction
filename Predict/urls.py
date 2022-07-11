from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.predict, name= "predict"),
    # path('/predict_price', views.predict_price, name= "predict_price")

]