from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TaskPhoto(models.Model):
    task = models.ForeignKey(Task, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='task_photos/')

    def __str__(self):
        return f"{self.task.title} - Photo {self.pk}"

