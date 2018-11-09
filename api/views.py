from rest_framework import generics
from api.models import User, Superadmin, Subadmin, Borrower, Facility, Equipment, Token, FacilityReservation, EquipmentReservation
from api.serializers import UserSerializer, TokenSerializer, SuperadminSerializer, SubadminSerializer, BorrowerSerializer, FacilitySerializer, EquipmentSerializer, FacilityReservationSerializer, EquipmentReservationSerializer

# TOKEN

class TokenList(generics.ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

# USER

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# SUPERADMIN

class SuperadminList(generics.ListCreateAPIView):
    serializer_class = SuperadminSerializer

    def get_queryset(self):
        queryset = Superadmin.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class SuperadminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superadmin.objects.all()
    serializer_class = SuperadminSerializer

# SUBADMIN

class SubadminList(generics.ListCreateAPIView):
    serializer_class = SubadminSerializer

    def get_queryset(self):
        queryset = Subadmin.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class SubadminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subadmin.objects.all()
    serializer_class = SubadminSerializer

# BORROWER

class BorrowerList(generics.ListCreateAPIView):
    serializer_class = BorrowerSerializer

    def get_queryset(self):
        queryset = Borrower.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

# FACILITY

class FacilityList(generics.ListCreateAPIView):
    serializer_class = FacilitySerializer

    def get_queryset(self):
        queryset = Facility.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

# EQUIPMENT

class EquipmentList(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


#FACILITY_RESERVATION

class FacilityReservationList(generics.ListCreateAPIView):
    serializer_class = FacilityReservationSerializer

    def get_queryset(self):
        queryset = FacilityReservation.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class FacilityReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacilityReservation.objects.all()
    serializer_class = FacilityReservationSerializer


#EQUIPMENT_RESERVATION

class EquipmentReservationList(generics.ListCreateAPIView):
    serializer_class = EquipmentReservationSerializer

    def get_queryset(self):
        queryset = EquipmentReservation.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class EquipmentReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentReservation.objects.all()
    serializer_class = EquipmentReservationSerializer