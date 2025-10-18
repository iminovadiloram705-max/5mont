from django.db import models

class Model(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='models/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
