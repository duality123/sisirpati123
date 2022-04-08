from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
	return render(request,'blog/beranda.html',{'test':2})


def pengaduan(request):
	return render(request,'blog/pengaduan.html',{'test':2})

def potensi(request):
	return render(request,'blog/potensi.html',{'test':2})

def profil(request):
	return render(request,'blog/profil.html',{'test':2})


def berita(request):
	return render(request,'blog/berita.html',{'test':2})