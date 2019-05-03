from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}' .format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField ('date created')
    due_on = models.DateTimeField ('due on')
    status = models.CharField(max_length=200) 
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)



    def __str__(self):
        return '{}: {}' .format(self.id, self.name, self.created_at, self.due_on, self.status, self.task_list)


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

# Create your models here.
