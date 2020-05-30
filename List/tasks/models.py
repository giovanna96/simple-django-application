from django.conf import settings
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now)
    deadline = models.DateField(blank=True, null=True)
    

    
    class Meta:
        ordering = ('created_date',)
    
    def __str__(self):
        return self.title