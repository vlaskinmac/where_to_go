from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_page),
    path('<int:place_id>/', views.get_place),
]