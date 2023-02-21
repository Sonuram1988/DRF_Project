from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.RDPStudentAPI.as_view()),
   
]