from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sejarahkampus.html/', views.sejarahkampus, name='sejarahkampus'),
    path('visimisi.html/', views.visimisi, name='visimisi'),
    path('hubungikami.html/', views.hubungikami, name='hubungikami'),
    path('fakultasteknik.html/', views.fakultasteknik, name='fakultasteknik'),
    path('fakultasmipa.html/', views.fakultasmipa, name='fakultasmipa'),
    path('fakultas_pai.html/', views.fakultas_pai, name='fakultas_pai'),
    path('fakultaspertanian.html/', views.fakultaspertanian, name='fakultaspertanian'),
    path('fakultasekonomi.html/', views.fakultasekonomi, name='fakultasekonomi'),
]





