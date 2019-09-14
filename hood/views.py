from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from hood.models import *
from hood.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
