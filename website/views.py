from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
	return render(request, 'index.html', {})

def amc(request):
	return render(request, 'amc.html', {})

def astro(request):
	return render(request, 'astro.html', {})

def cops(request):
	return render(request, 'cops.html', {})

def csi(request):
	return render(request, 'csi.html', {})

def robotics(request):
	return render(request, 'robotics.html', {})

def sae(request):
	return render(request, 'sae.html', {})

def biz(request):
	return render(request, 'biz.html', {})

def team(request):
	return render(request, 'team.html', {})

def inventory(request):
        return render(request, 'inventory.html', {})

def inventory(request):
        return render(request, 'tac.html', {})

def learning(request):
        return render(request, 'learning.html', {})

def app(request):
	return HttpResponseRedirect("https://play.google.com/store/apps/details?id=in.shriyansh.questify&hl=en")
