from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert/', views.insert_data, name='insert_data'),

]
