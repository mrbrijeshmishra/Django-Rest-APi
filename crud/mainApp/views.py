from django.shortcuts import render
from .serializers import Student
from .models import student
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import student
from .serializers import Student
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_info(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Student(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Data received successfully"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        else:
            res = {"msg":"Data incorrect"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
    
@csrf_exempt
def get_student(request):
    data = student.objects.all()
    stream = Student(data,many=True)
    json_data = JSONRenderer().render(stream.data)
    return HttpResponse(json_data,content_type="application/json")


@csrf_exempt
def update_record(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    try:
        stud = student.objects.get(roll = pythondata['roll'])
        stu_serializer = Student(stud,data=pythondata,partial=True)
        if stu_serializer.is_valid():
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            res = {'msg':'Data sent wrong'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
    except:
        res = {'msg':'Something went wrong'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')