from django import forms
from multiupload.fields import MultiFileField
from .models import Task, TaskPhoto

class PhotoForm(forms.ModelForm):
    class Meta:
        model = TaskPhoto
        fields = ['photo']

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete', 'assigned_user']

    photos = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5, required=False, label='Photos')

    def save(self, commit=True):
        task = super().save(commit)
        photos = self.cleaned_data.get('photos', [])
        
        if photos:
            for photo in photos:
                TaskPhoto.objects.create(task=task, photo=photo)

        return task
