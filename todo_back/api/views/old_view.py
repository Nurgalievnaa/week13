import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList
from api.serializers import TaskListSerializer, TaskSerializer, TaskListSerializer2


@csrf_exempt
def tasklists_show(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})





@csrf_exempt
def tasklist_detail(request, pk):
    try:
        oneTaskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = TaskListSerializer(oneTaskList)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=oneTaskList, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        oneTaskList.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})





def tasklist_tasks(request, pk):
    try:
        oneTaskList=TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks=oneTaskList.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)