from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,request,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
# single student data

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    # print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

    # return JsonResponse(serializer.data,safe=True)

# query set-Al student data
def students_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    # print(serializer.data)

    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')

    # this is another way to create response
    return JsonResponse(serializer.data,safe=False)






