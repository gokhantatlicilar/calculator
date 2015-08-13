from django.shortcuts import render,HttpResponse,redirect
from django.contrib.staticfiles import storage

def main(request):
    return render(request, 'oriflame.html')

def css_examples(request):
	return render(request, 'css_examples.html')