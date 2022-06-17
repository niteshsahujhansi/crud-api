# from enroll.models import User
# from enroll.api.serializers import UserSerializer
# from rest_framework import viewsets

# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


# //////////////////////////////////////////////////////////////////////////////////////////////////

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from .models import Student
from enroll.models import User
# from .serializers import StudentSerializer
from enroll.api.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = User.objects.get(id=id)
            serializer = UserSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = User.objects.all()
        serializer = UserSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = UserSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = User.objects.get(id=id)
        serializer = UserSerializer(stu, data = pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = User.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

