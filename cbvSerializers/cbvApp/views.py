from django.shortcuts import render,get_object_or_404
from django.http import Http404
from cbvApp.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework import mixins,generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

class StudentPagination(PageNumberPagination):
    page_size = 1

# Create your views here.

# Viewsets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = StudentPagination
    pagination_class = LimitOffsetPagination
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]


# Generics View
# class StudentClassList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# Mixin ( Generic API View )
# class StudentClassList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class StudentDetail(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(reuest,pk)

# APIView ( Class Based Views )
# class StudentClassList(APIView):
#     def get(self,request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         seializer = StudentSerailzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class StudentDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return get_object_or_404(Student,pk=pk)
#         except:
#             raise Http404
#
#     def get(self,request,pk):
#         student = self.get_object(pk=pk)
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer)
#
#     def put(self,request,pk):
#         student = self.get_object(pk=pk)
#         serializer = StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serailzer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         student = self.get_object(pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
