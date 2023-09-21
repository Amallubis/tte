from django.shortcuts import render, redirect
from django.contrib import messages
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
    listpengaduan = Pengaduan.objects.all().order_by('-pk')
    return render(request,'backend/list-pengaduan.html',{'listpengaduan':listpengaduan})

def  hapuspengaduan(request, id_hapus):
    pengaduan = Pengaduan.objects.filter(id= id_hapus)
    pengaduan.delete()
    messages.success(request,'Data berhasil dihapus')
    return redirect('list-pengaduan')   
    
def addpost(request):
    if request.POST:
        judul = request.POST.get('judul')
        posting = request.POST.get('posting')
        images = request.FILES.getlist('images')
        for img in images:
            Berita.objects.create(fotos=img)
        if judul =="" or posting == "":
            messages.error(request,'Tidak boleh kosong')
        i = Berita(judul=judul, postingan =posting)
    i = Berita.objects.all()
    return render(request,'backend/addpost.html',{'i':i})

            
                