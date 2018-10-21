from rest_framework import generics
from api.models import Superadmin, Subadmin, Borrower, Facility, Equipment, Token
from api.serializers import TokenSerializer, SuperadminSerializer, SubadminSerializer, BorrowerSerializer, FacilitySerializer, EquipmentSerializer

# TOKEN

class TokenList(generics.ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

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