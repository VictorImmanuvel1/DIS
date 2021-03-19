from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('adminLogin/', views.adminLogin),
    path('staffLogin/', views.staffLogin),
    path('adminHome/', views.admin),
    path('staff/', views.staff),
    path('event/', views.event),
    path('staffDetails/',views.staffdet),
    path('staffReg/',views.staffreg),
    path('studentDetails/',views.studentdet),
    path('studentReg/',views.studentreg),
]