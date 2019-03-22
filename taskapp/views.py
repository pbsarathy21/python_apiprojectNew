from typing import Any

from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer

    def retrieve(self, request: Request, *args: Any, **kwargs: Any):

        instance = self.get_object()

        serializer = self.get_serializer(instance)

        my_json = {'status': True, 'msg': 'success', 'data': serializer.data}

        return Response(my_json)

    def list(self, request: Request, *args: Any, **kwargs: Any):

        instance = Task.objects.all()

        serializer = self.get_serializer(instance)

        return Response({'something': 'my custom JSON', 'data': serializer.data})

    def update(self, request: Request, *args: Any, **kwargs: Any):

        value = request.POST.get("task_name", "")

        return Response({'value': value})

    def create(self, request: Request, *args: Any, **kwargs: Any):

        task_name = request.POST.get("task_name", "")
        task_desc = request.POST.get("task_desc", "")

        if not task_name:
            return Response({'empty data': 'task_name'})
        elif not task_desc:
            return Response({'empty data': 'task_desc'})
        else:
            instance = Task.objects.create(task_name=task_name, task_desc=task_desc)
            value = self.get_object()
            serializer = self.get_serializer(value)
            return Response({'data': serializer.data})

