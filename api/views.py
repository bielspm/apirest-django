from django.shortcuts import render
from api.models import Dog
from api.serializers import DogSerializer
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404

json_response = {'status_code': '', 'message': '', 'data': ''}
@csrf_exempt
def dog_store(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    data = JSONParser().parse(request)
    serializer = DogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def dog_delete(request, id):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed(['DELETE'])
    dog = get_object_or_404(Dog, id=id)
    dog.delete()
    return JsonResponse({'response_txt': 'Deletado com sucesso'}, status=200)

@csrf_exempt
def dog_update(request, id):
    if request.method != 'PATCH':
        return HttpResponseNotAllowed(['PATCH'])
    data = JSONParser().parse(request)
    print(data)
    dog = get_object_or_404(Dog, id=id)
    serializer = DogSerializer(instance=dog, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)

@csrf_exempt
def dog_show(request, id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    dog = get_object_or_404(Dog, id=id)
    serializer = DogSerializer(dog)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def dog_index(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return JsonResponse(serializer.data, safe=False)
