from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('breakfast', views.breakfast, name="breakfast"),
    path('lunch', views.lunch, name="lunch"),
    path('dinner', views.dinner, name="dinner"),
]