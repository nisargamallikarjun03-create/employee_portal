from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:id>/', views.employee_detail, name='employee_detail'),
]