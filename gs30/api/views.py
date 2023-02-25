from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes=[ScopedRateThrottle]
  throttle_scope='viewstu'

class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes=[ScopedRateThrottle]
  throttle_scope='viewcreate'

  

class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes=[ScopedRateThrottle]
  throttle_scope='viewstu'

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes=[ScopedRateThrottle]
  throttle_scope='viewupdate'

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes=[ScopedRateThrottle]
  throttle_scope='viewdestroy'
