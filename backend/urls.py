from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    # path('heart/',views.heart),
    # path('lungs/',views.lungs),
    # path('heart/heart-result/',views.hresult),
]