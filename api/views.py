from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Superadmin, Subadmin, Borrower, Facility, Equipment
from api.serializers import SuperadminSerializer, SubadminSerializer, BorrowerSerializer, FacilitySerializer, EquipmentSerializer

# Create your views here.

@csrf_exempt
def superadmin_list(request):
    if request.method == 'GET':
        superadmins = Superadmin.objects.all()
        serializer = SuperadminSerializer(superadmins, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuperadminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def superadmin_detail(request, pk):
    try:
        superadmin = Superadmin.objects.get(pk=pk)
    except Superadmin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SuperadminSerializer(superadmin)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SuperadminSerializer(superadmin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        superadmin.delete()
        return HttpResponse(status=204)

@csrf_exempt
def subadmin_list(request):
    if request.method == 'GET':
        subadmins = Subadmin.objects.all()
        serializer = SubadminSerializer(subadmins, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubadminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def subadmin_detail(request, pk):
    try:
        subadmin = Subadmin.objects.get(pk=pk)
    except Subadmin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SubadminSerializer(subadmin)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubadminSerializer(subadmin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        subadmin.delete()
        return HttpResponse(status=204)

@csrf_exempt
def borrower_list(request):
    if request.method == 'GET':
        borrowers = Borrower.objects.all()
        serializer = BorrowerSerializer(borrowers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BorrowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def borrower_detail(request, pk):
    try:
        borrower = Borrower.objects.get(pk=pk)
    except Borrower.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BorrowerSerializer(borrower)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BorrowerSerializer(borrower, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        borrower.delete()
        return HttpResponse(status=204)

@csrf_exempt
def facility_list(request):
    if request.method == 'GET':
        facilities = Facility.objects.all()
        serializer = FacilitySerializer(facilities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FacilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def facility_detail(request, pk):
    try:
        facility = Facility.objects.get(pk=pk)
    except Facility.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FacilitySerializer(facility)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FacilitySerializer(facility, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        facility.delete()
        return HttpResponse(status=204)

@csrf_exempt
def equipment_list(request):
    if request.method == 'GET':
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EquipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def equipment_detail(request, pk):
    try:
        equipment = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EquipmentSerializer(equipment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EquipmentSerializer(equipment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        equipment.delete()
        return HttpResponse(status=204)