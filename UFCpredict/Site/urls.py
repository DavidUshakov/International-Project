from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('about', views.about),
    path('index', views.index),
    path('prediction', views.predPage),
]
