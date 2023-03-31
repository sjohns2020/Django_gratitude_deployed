from django.db import models
from django.utils import timezone

class Org(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()
    upload = models.ImageField(upload_to='uploads/', default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLrWVtomuKNMXY38fiZ6HM7PJSiE7ubfdfvQbdAXC9&s")

    def __str__(self):
        return self.name