from typing import Any

from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


# Create your views here.

class TaskViewSet(APIView):
    @staticmethod
    def get(request):
        value = Task.objects.all()
        my_list = []

        for x in value:
            my_dict = {'id': x.id, 'task_name': x.task_name, 'task_desc': x.task_desc}
            my_list.append(my_dict)

        return Response({'data': my_list})

    @staticmethod
    def post(request):

        name = request.POST.get("task_name", "")
        desc = request.POST.get("task_desc", "")

        if not name:
            return Response({'status': 'error', 'message': 'The required fields are task_name and task_desc'})
        elif not desc:
            return Response({'status': 'error', 'message': 'The required fields are task_name and task_desc'})
        elif Task.objects.filter(task_name=name).exists():
            return Response({'status': 'error', 'message': 'task_name already exists'})
        else:
            data = Task.objects.create(task_name=name, task_desc=desc)
            my_data = {'id': data.id, 'task_name':data.task_name, 'task_desc': data.task_desc}
            my_list = [my_data]
            return Response({'data': my_list})



    # def retrieve(self, request: Request, *args: Any, **kwargs: Any):
    #
    #     instance = self.get_object()
    #
    #     serializer = self.get_serializer(instance)
    #
    #     my_json = {'status': True, 'msg': 'success', 'data': serializer.data}
    #
    #     return Response(my_json)
    #
    # def list(self, request: Request, *args: Any, **kwargs: Any):
    #
    #     instance = Task.objects.all()
    #
    #     serializer = self.get_serializer(instance)
    #
    #     return Response({'something': 'my custom JSON', 'data': serializer.data})
    #
    # def update(self, request: Request, *args: Any, **kwargs: Any):
    #
    #     value = request.POST.get("task_name", "")
    #
    #     return Response({'value': value})

    # def create(self, request: Request, *args: Any, **kwargs: Any):
    #
    #     task_name = request.POST.get("task_name", "")
    #     task_desc = request.POST.get("task_desc", "")
    #
    #     if not task_name:
    #         return Response({'empty data': 'task_name'})
    #     elif not task_desc:
    #         return Response({'empty data': 'task_desc'})
    #     else:
    #         instance = Task.objects.create(task_name=task_name, task_desc=task_desc)
    #         value = self.get_object()
    #         serializer = self.get_serializer(value)
    #         return Response({'data': serializer.data})
