from django.urls import path
from backend import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list-pengaduan/', views.listpengaduan, name='list-pengaduan'),
    path('hapus-pengaduan/<int:id_hapus>/', views.hapuspengaduan, name='hapus-pengaduan'),
    #posting news 
    path('addpost/', views.addpost, name='addpost'),
]
