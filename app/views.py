from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

	# template = 'app/index.html'
	template = 'pure_html/app/index.html'
	context_dict = {}
	return render(request, template, context_dict)
	# return HttpResponse("App Index Page")