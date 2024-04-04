from django.db import models

class Request(models.Model):
    request_data = models.TextField()
    time_received = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True)