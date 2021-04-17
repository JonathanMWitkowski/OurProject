from django.shortcuts import render
import requests

# Create your views here.
def HomeView(request):
	return render(request, 'project/home.html', {})