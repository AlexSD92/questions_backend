from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s question"
