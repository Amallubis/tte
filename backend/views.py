from django.shortcuts import render
from django.contrib import messages
from django.forms import formset_factory
from beranda.models import Pengaduan
from backend.models import Berita
from backend.forms import FormPost


# Create your views here.

def dashboard(request):
    pengaduan = Pengaduan.objects.count()
    context ={
        'title':'Dashboard',
        'pengaduan':pengaduan
    }
    return render(request,'backend/dashboard.html',context)

    
def listpengaduan(request):
    listpengaduan = Pengaduan.objects.all()
    return render(request,'backend/list-pengaduan.html',{'listpengaduan':listpengaduan})

    
    
def addpost(request):
    if request.POST:
        images = request.FILES.getlist('images')
        for img in images:
            Berita.objects.create(fotos=img)
    images = Berita.objects.all()
    return render(request,'backend/addpost.html',{'images':images})
            
                