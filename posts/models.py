from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from orgs.models import Org


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=255)
    message = models.TextField()
    company = models.ForeignKey(Org, null=True, on_delete=models.CASCADE, related_name="company")
    recipients = models.ManyToManyField(User, related_name="recipients")
    visit_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    post_date = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()
    upload = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title