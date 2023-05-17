from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializer import*
from rest_framework import status

@api_view(['GET','POST','DELETE','PUT','PATCH'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu=Student.objects.get(id=id)
            ser=StudentSerializer(stu)
            return Response(ser.data)
        stu=Student.objects.all()
        ser=StudentSerializer(stu,many=True)
        return Response(ser.data)
        
    elif request.method == 'POST':
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'data created successfully'})
        return Response(ser.errors)
    
    elif request.method == 'PUT':
        id=pk
        stu=Student.objects.get(pk=id)
        ser=StudentSerializer(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'data updated successfully'})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        id=pk
        stu=Student.objects.get(pk=id)
        ser=StudentSerializer(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg': 'Patch data updated successfully'})
        return Response(ser.errors)
    

    elif request.method == 'DELETE':
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'data deleted successfully'})
        


