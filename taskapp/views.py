from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task


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
        image_save = request.FILES.get("image")
        # image.save()


        if not name:
            return Response({'status': 'error', 'message': 'The required fields are task_name and task_desc'})
        elif not desc:
            return Response({'status': 'error', 'message': 'The required fields are task_name and task_desc'})
        elif Task.objects.filter(task_name=name).exists():
            return Response({'status': 'error', 'message': 'task_name already exists'})
        else:
            data = Task.objects.create(task_name=name, task_desc=desc, image=image_save)
            my_data = {'id': data.id, 'task_name':data.task_name, 'task_desc': data.task_desc}
            # data = Task.objects.create(task_name=name, task_desc=desc)
            # my_data = {'id': data.id, 'task_name': data.task_name, 'task_desc': data.task_desc}
            my_list = [my_data]

            try:
                from PIL import Image, ImageOps
            except ImportError:
                import Image
                import ImageOps
            image = Image.open(image_save)
            imageresize = image.resize((600, 600), Image.ANTIALIAS)
            image_url = 'taskapp/media/images/' + 'hai.png'
            imageresize.save(image_url, quality=75)

            return Response({'image': image_url, 'data': my_list})

    @staticmethod
    def update(request, pk):
        return Response({'status': 'success', 'message': 'updated'})


class Path(APIView):
    def get(self, request, pk):
        try:
            data = Task.objects.get(id=pk)
            return Response({'task_name': data.task_name})
        except Task.DoesNotExist:
            return Response({'error': 'no data found'})

    def delete(self, request, pk):
        try:
            data = Task.objects.filter(id=pk).delete()
            return Response({'messages': 'deleted successfully'})
        except Task.DoesNotExist:
            return Response({'error': 'no data found'})

    def update(self, request):
        id_value = request.PUT.get("id", "")
        name = request.PUT.get("task_name", "")
        desc = request.PUT.get("task_desc", "")

        if not id_value:
            return Response({'message': 'id is missing'})
        elif not name or not desc:
            return Response({'message': 'please specify values to update'})
        else:
            try:
                update = Task.objects.get(id=id_value)
                update.task_name = name
                update.task_desc = desc

                value = Task.objects.get(id=id_value)
                my_list = [{'id': value.id, 'task_name': value.task_name, 'task_desc': value.task_desc}]
                return Response({'message': 'updated successfully', 'data': my_list})
            except Task.DoesNotExist:
                return Response({'message': 'no data exists'})


class TaskApi(APIView):
    @staticmethod
    def get(request):
        data = Task.objects.all()
        my_list = []
        for x in data:
            my_dict = {'id': x.id,
                       'task_name': x.task_name,
                       'task_desc': x.task_desc}
            my_list.append(my_dict)
        return Response({'data': my_list})

    def update(self, request):
        id_value = request.PUT.get("id", "")
        name = request.PUT.get("task_name", "")
        desc = request.PUT.get("task_desc", "")

        if not id_value:
            return Response({'message': 'id is missing'})
        elif not name or not desc:
            return Response({'message': 'please specify values to update'})
        else:
            try:
                update = Task.objects.get(id=id_value)
                update.task_name = name
                update.task_desc = desc

                value = Task.objects.get(id=id_value)
                my_list = [{'id': value.id, 'task_name': value.task_name, 'task_desc': value.task_desc}]
                return Response({'message': 'updated successfully', 'data': my_list})
            except Task.DoesNotExist:
                return Response({'message': 'no data exists'})


    # def put(self, request, pk):

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
