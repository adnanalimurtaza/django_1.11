from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request): #retrieve
	# instance = Post.objects.get(id=5)
	instance = get_object_or_404(Post, id = 1)
	context  = {
		"title" : instance.title,
		"instance":instance
	}
	return render(request, "post_detail.html", context)

def post_list(request): #list items
	queryset = Post.objects.all()
	context  = {
		"queryset":queryset,
		"title" : "List"
	}		
	
	# if request.user.is_authenticated():
	# 	context  = {
	# 		"title" : "User list"
	# 	}
	# else:
	# 	context  = {
	# 		"title" : "List"
	# 	}
	return render(request, "index.html", context)
	# return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
