
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('heart/', views.heart, name = 'heart'),
    path('kidney/', views.kidney, name = 'kidney'),
    path('diabetes/',views.diabetes, name = 'diabetes'),
    path('liver/',views.liver, name = 'liver'),
    path('heart/hpredict', views.hdpredictor, name = 'hpredict'),
    path('kidney/kpredict', views.kdpredictor, name = 'kpredict'),
    path('diabetes/dbpredict', views.dbpredictor, name = 'diabetes_pred'),
    path('liver/lpredict', views.lpredictor, name = 'lpredict'),
]
