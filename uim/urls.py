from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sejarahkampus.html/', views.sejarahkampus, name='sejarahkampus'),
    path('visimisi.html/', views.visimisi, name='visimisi'),
    path('hubungikami.html/', views.hubungikami, name='hubungikami'),
]




