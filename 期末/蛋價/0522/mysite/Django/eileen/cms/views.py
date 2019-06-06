from django.shortcuts import render_to_response
# Create your views here.
from .models import egg

def index(request):
	eggs = egg.objects.all()
	return render_to_response('cms/menu.html',locals())
