from django.urls import path
from backend import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list-pengaduan/', views.listpengaduan, name='list-pengaduan')
]
