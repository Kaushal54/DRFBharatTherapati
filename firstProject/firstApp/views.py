from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from .task import json_response
# Create your views here.
def employeeView(request):
    emp = {
        'id':123,
        'name':'john',
        'salary':'1000000',
    }

    data = Employee.objects.all()
    response = {'employee':list(data.values('id','name','sal'))}
    return JsonResponse(response)

@csrf_exempt
def create_emp(request):
    if request.method == "POST":
        print("*** post req ***")
        data = {}
        message = 'Post Req'

        response = json_response(request,'success','200',message,data)
        # response = json_response(request,'error','404',message,data)
        return JsonResponse(response)
