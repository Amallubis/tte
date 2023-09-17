from django.shortcuts import render
from beranda.models import Pengaduan
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