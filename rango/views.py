from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
	context_list = Category.objects.order_by('-likes')
	context_dict = {'categories': context_list}
	
	return render(request, 'rango/index.html', context_dict)
	# return HttpResponse("Hello, world")

def about(request):
	return render(request, 'rango/about.html')
	
def category(request, category_name_slug):
	context_dict = {}
	
	try:
