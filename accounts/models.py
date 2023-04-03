from django.db import models
from django.contrib.auth.models import User
from orgs.models import Org
from posts.models import Post


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    organisations = models.ManyToManyField(
        Org, related_name="organisations"
    )
    stars = models.IntegerField(default=0)
    # posts = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="author")
    pic = models.ImageField(upload_to='uploads/', default="https://i.pinimg.com/originals/3d/66/78/3d667893c5788613ff3590ca218a9cb2.jpg")

    

    def __str__(self):
        return self.user.username
    

    def add_stars(self, stars):
        print(stars)
        print(self.stars)
        self.stars += int(stars)