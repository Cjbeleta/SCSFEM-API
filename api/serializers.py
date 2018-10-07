from .models import Superadmin, Subadmin, Borrower, Facility, Equipment,Token
from rest_framework import serializers

class SuperadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superadmin
        fields = ('id', 'name', 'email', 'token_id')

    # THIS IS SAMPLE CODE FOR USING serializers.Serializers

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # token_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    # def create(self, validated_data):
    #     return Superadmin.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

    # END OF SAMPLE

class SubadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subadmin
        fields = ('id', 'name', 'email', 'token_id')

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # token_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    # def create(self, validated_data):
    #     return Subadmin.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('id', 'name', 'email', 'token_id')

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # token_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    # def create(self, validated_data):
    #     return Borrower.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'name', 'status', 'date_added','borrower_id')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'status', 'date_added', 'borrower_id')