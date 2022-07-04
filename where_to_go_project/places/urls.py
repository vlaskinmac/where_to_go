from django.urls import path

from . import views

urlpatterns = [
    # path('<placeId>', views.index),
    path('place/', views.index),
]