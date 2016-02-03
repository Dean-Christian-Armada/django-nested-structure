from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

	# template = 'app/subapp1/index.html'
	template = 'pure_html/app/subapp1/index.html'
	context_dict = {}
	return render(request, template, context_dict)
	# return HttpResponse("Sub App 1 Index Page")