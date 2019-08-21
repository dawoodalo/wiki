from django.shortcuts import render
from .models import Page

def list(request):
	context= {

		"plist": Page.objects.all(),
	}
	return render(request, "list.html", context)
	

def detail(request, page_id ):
	context= {

		"dlist": Page.objects.get(id=page_id),
	}
	return render(request, "details.html", context)
	 