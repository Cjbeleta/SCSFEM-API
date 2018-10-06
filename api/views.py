from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Superadmin, Subadmin, Borrower
from api.serializers import SuperadminSerializer, SubadminSerializer, BorrowerSerializer

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
        