from .models import User, Superadmin, Subadmin, Borrower, Facility, Equipment,Token, FacilityReservation, EquipmentReservation
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'token', 'ttl')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'usertype',)

class SuperadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superadmin
        fields = ('id', 'name', 'email', 'token_id')

class SubadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subadmin
        fields = ('id', 'name', 'email', 'token_id')

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('id', 'name', 'email', 'token_id')

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'name', 'status', 'date_added','borrower_id')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'status', 'quantity', 'date_added', 'borrower_id')

class FacilityReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityReservation
        fields = ('id', 'borrower_id', 'facility_id', 'date_application', 'date_reservation_start', 'date_reservation_end', 'status')

class EquipmentReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentReservation
        fields = ('id', 'borrower_id', 'equipment_id', 'quantity', 'date_application', 'date_reservation_start', 'date_reservation_end', 'status')

