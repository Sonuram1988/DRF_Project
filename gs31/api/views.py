from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    # print(queryset)
    serializer_class=StudentSerializer

    def get_queryset(self):
        #current user
        user=self.request.user
        return Student.objects.filter(passby=user)



