from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import TaskList


def task_lists_sh(request):
    TaskLists=TaskList.objects.all()
    json_TaskLists = [t.to_json() for t in TaskLists]
    return JsonResponse(json_TaskLists, safe=False)




# Create your views here.
def task_lists_detail(request, pk):
    taskon=TaskList.objects.get(id=pk)
    return JsonResponse(taskon.to_json())



def tasklist_tasks(request,pk):
    try:
        onetask=TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)}, safe=False)

    tasks=onetask.task_set.all()
    json_tasks=[t.to_json() for t in tasks]
    return JsonResponse(json_tasks,safe=False)
