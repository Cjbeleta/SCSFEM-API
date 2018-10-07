from django.urls import path
from api import views

urlpatterns = [
    path('api/superadmin/', views.superadmin_list),
    path('api/superadmin/<int:pk>/', views.superadmin_detail),
    path('api/subadmin/', views.subadmin_list),
    path('api/subadmin/<int:pk>/', views.subadmin_detail),
    path('api/borrower/', views.borrower_list),
    path('api/borrower/<int:pk>/', views.borrower_detail),
    path('api/facility/', views.facility_list),
    path('api/facility/<int:pk>/', views.facility_detail),
    path('api/equipment/', views.equipment_list),
    path('api/equipment/<int:pk>/', views.equipment_detail)
]