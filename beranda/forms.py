from django.forms import ModelForm
from beranda.models import Pengaduan


class FormPengaduan(ModelForm):
    class Meta:
        model = Pengaduan
        fields = '__all__'

