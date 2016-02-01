from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

	# template = 'login/index.html'
	template = 'pure_html/login/index.html'
	context_dict = {}
	context_dict['title'] = "Log-In Page"
	return render(request, template, context_dict)
	# return HttpResponse("Index")

def logout(request):
	return HttpResponse("Logout")