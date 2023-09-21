from django.shortcuts import render
from django.contrib import messages
from beranda.models import Pengaduan
from beranda.forms import FormPengaduan
from backend.models import Berita

# Create your views here.

def beranda(request):
    i = Berita.objects.all().order_by('-pk')
    context={
        'i':i,
        'title':'TTE Deli Serdang'
    }
    return render(request,'beranda/beranda.html',context)

    
def tambahpengaduan(request):
    if request.POST:
        form = FormPengaduan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Pengaduan Anda Berhasil dikirim, Tim TTE akan menghubungi Anda')
            return render(request,'beranda/tambah-pengaduan.html',{'form':form})
    else:
        form =FormPengaduan()
        return render(request,'beranda/tambah-pengaduan.html',{'form':form})

        
def  hapuspengaduan(request, id_hapus):
    pengaduan = Pengaduan.objects.filter(id= id_hapus)
    pengaduan.delete()
    messages.success(request,'Data berhasil dihapus')

    
    
            