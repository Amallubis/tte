from django.shortcuts import render
from django.contrib import messages
from beranda.forms import FormPengaduan

# Create your views here.

def beranda(request):
    context={
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
            