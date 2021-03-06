from .models import User, Superadmin, Subadmin, Borrower, Facility, Equipment,Token, Reservation, Schedule, Logs
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'token', 'ttl')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'date_added' ,'email', 'usertype',)

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
        fields = ('id', 'borrower_id', 'item_id', 'reserve_type', 'eventname', 'quantity', 'date_application', 'year', 'month', 'start_day', 'end_day', 'start_time', 'end_time', 'remarks', 'status')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'info', 'day', 'month', 'year', 'time_start', 'time_end', 'item_type', 'item_id')

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('id', 'date', 'borrower', 'admin', 'message') 