from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/token/', views.TokenList.as_view()),
    path('api/user/', views.UserList.as_view()),
    path('api/user/<int:pk>/', views.UserDetail.as_view()),
    path('api/superadmin/', views.SuperadminList.as_view()),
    path('api/superadmin/<int:pk>/', views.SuperadminDetail.as_view()),
    path('api/subadmin/', views.SubadminList.as_view()),
    path('api/subadmin/<int:pk>/', views.SubadminDetail.as_view()),
    path('api/borrower/', views.BorrowerList.as_view()),
    path('api/borrower/<int:pk>/', views.BorrowerDetail.as_view()),
    path('api/facility/', views.FacilityList.as_view()),
    path('api/facility/<int:pk>/', views.FacilityDetail.as_view()),
    path('api/equipment/', views.EquipmentList.as_view()),
    path('api/equipment/<int:pk>/', views.EquipmentDetail.as_view()),
    path('api/facilityreservation/', views.FacilityReservationList.as_view()),
    path('api/facilityreservation/<int:pk>/', views.FacilityReservationDetail.as_view()),
    path('api/equipmentreservation/', views.EquipmentReservationList.as_view()),
    path('api/equipmentreservation/<int:pk>/', views.EquipmentReservationDetail.as_view())
    ]

urlpatterns = format_suffix_patterns(urlpatterns)