from django.test import TestCase

from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone
# Create your tests here.
# profile test
class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='tony')
        # save user
        self.user.save()
        self.profile = Profile(photo='black and white',bio='test bio',contact="abc@xyz.com",user=self.user)
        self.profile.save_profile()


    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
           # saving profile
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        #    delete test
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)
            #  post test classtesting post
class PostTestClass(TestCase):
        #  new post
    def setUp(self):
        self.post = post(title ='new post', image='image.url',description="awwaaards",link="http://www.awwaards.com")

    def tearDown(self):
        post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, post))
            # save method
    def test_save_method(self):
        self.post.save_post()
        posts = post.objects.all()
        self.assertTrue(len(posts)>0)
        # delete post test
    def test_delete_method(self):
        self.post.save_post()
        posts = post.objects.all()
        self.post.delete_post()
        posts = post.objects.all()
        self.assertTrue(len(posts)==0)
            #   ReviewTestClass
class ReviewTestClass(TestCase):
    def setUp(self):
        # self.post=post(caption="test iamge",likes=1)
        self.user = User(username='tony')
        self.user.save()
        self.post = post(title ='new post', image='image.url',description="awwaaards",link="http://www.awwaards.com")
        self.post.save_post()

        self.new_review=Review(design="9",usability="9",content="10",user=self.user,post=self.post)
        self.new_review.save_review()

    def tearDown(self):
        Review.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
            # save comment
    def test_save_comment(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)
       # delete comment
    def test_delete_comment(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)==0)
