from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

	# template = 'login/index.html'
	template = 'pure_html/login/index.html'
	context_dict = {}
	return render(request, template, context_dict)
	# return HttpResponse("Index Page")

def logout(request):
	return HttpResponse("Logout")