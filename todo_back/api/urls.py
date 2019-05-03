from django.urls import path
from api import views

urlpatterns=[
    path('tasklists/',views.task_lists_sh),
    path('tasklists/<int:pk>/', views.task_lists_detail),
    path('tasklists/<int:pk>/tasks/', views.tasklist_tasks)
]
