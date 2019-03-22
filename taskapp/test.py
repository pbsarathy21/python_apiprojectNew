from django.http import JsonResponse

from .models import Task


def test(request):

    my_query = Task.objects.all()

    my_array = []

    for x in my_query:
        new_dict = {'id': x.id, 'task_name': x.task_name, 'task_desc': x.task_desc, 'date_created': x.date_created}
        my_array.append(new_dict)

    my_dict = {'status': 'success', 'msg': True, 'data': my_array}
    return JsonResponse(my_dict, status=200)
