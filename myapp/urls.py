from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('duyurular/', views.announcements_view, name='announcements'),
]