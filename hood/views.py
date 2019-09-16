from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from hood.models import *
from hood.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import  *
# from .serializer import *
# from .permissions import IsAdminOrReadOnly
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse






def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration.html', {'form': form})

@login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"

    profiles = Profile.objects.all()
    posts = Post.objects.all()
    # reviews = Review.objects.all()

    context ={"profiles":profiles,"posts":posts,"message":message}

    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    
    users = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()

    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)


    posts = Post.get_profile_pic(profile.id)
    return render(request, 'registration/profile.html', {'title':title,'profile':profile,"posts":posts, 'profile_info':profile_info,"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):

    profile = User.objects.get(username=request.user)
    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            # return HttpResponseRedirect(reverse('profile', username=request.user))

            return redirect('profile', username=request.user)
    else:
        form = ProfileForm()

    return render(request, 'registration/update_profile.html', {'form':form, 'profile_info':profile_info})

@login_required(login_url='/accounts/login')
def new_post(request):
	current_user = request.user
	if request.method == 'POST':
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.user = current_user
			new_post.save()
            # messages.success(request, "Image uploaded!")
			return redirect('index')
	else:
			form = PostForm()
            # context= {"form":form}
	return render(request, 'post.html',{"form":form})

@login_required(login_url='/accounts/login')
def post_details(request,id):
    post = Post.objects.get(id = id)
    # reviews = Review.objects.order_by('-timestamp')

    context={"post":post}
    return render(request, 'post_details.html',context)

# Create your views here.
@login_required(login_url='/accounts/login')
def search(request):
    if 'business' in request.GET and request.GET['business']:
        profile = UserProfile.objects.get(user = request.user)
        search_term = request.GET.get('business')
        results = Business.objects.filter(neighbourhood = profile.neighbourhood, name__icontains = search_term)
        message = f'{search_term}'
        context = {
            'message': message,
            'results': results
        }
        
    return render(request, 'search.html', context)
@login_required(login_url='/accounts/login')
def business(request):
	current_user = request.user
    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
    context = {
        'businesses': businesses
     }    
    return render(request, 'business.html', context)
@login_required(login_url='/accounts/login')
def new_business(request):
    profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = profile
            business.neighbourhood = profile.neighbourhood
            business.save()
        return redirect('business')
    else:
        form = BusinessForm()
    context = {
        'form': form
    }
    return render(request, 'new_business.html', context)

