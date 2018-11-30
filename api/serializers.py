from .models import User, Superadmin, Subadmin, Borrower, Facility, Equipment,Token, Reservation
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
        fields = ('id', 'name', 'description', 'image', 'status', 'date_added','borrower_id')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'description', 'image', 'status', 'quantity', 'date_added', 'borrower_id')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'borrower_id', 'item_id', 'reservation_type', 'date_application', 'date_reservation_start', 'date_reservation_end', 'status')
