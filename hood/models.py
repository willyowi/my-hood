from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# import numpy as np
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(upload_to='profpics/',default='NO IMAGE')
    bio = HTMLField()
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)
    contact = models.CharField(max_length=60,blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    timestamp = models.DateTimeField(default=timezone.now())
    # timestamp = models.DateTimeField(auto_now_add=True,null = True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

class Post(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = models.ImageField(upload_to='projectpics/',default='NO IMAGE')
    description = HTMLField()
    
    # link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    
    # def avg_design(self):
    #     design_reviews = list(map(lambda x: x.design, self.review_set.all()))
    #     return np.mean(design_reviews)
    # def avg_content(self):
    #     content_reviews = list(map(lambda x: x.content, self.review_set.all()))
    #     return np.mean(content_reviews)
    # def avg_usability(self):
    #     usability_reviews = list(map(lambda x: x.usability, self.review_set.all()))
    #     return np.mean(usability_reviews)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def postt_by_id(cls,id):
        project = Post.objects.filter(id =id)
        return project

    @classmethod
    def get_posts(cls):
        posts = Post.objects.all()
        return posts

    @classmethod
    def get_profile_pic(cls,profile):
        posts = Post.objects.filter(profile__pk = profile)
        return posts
    @classmethod
    def search_by_title(cls,search_term):
    	posts = cls.objects.filter(title__icontains=search_term)
    	return posts

    class Meta:
        ordering = ['-timestamp']