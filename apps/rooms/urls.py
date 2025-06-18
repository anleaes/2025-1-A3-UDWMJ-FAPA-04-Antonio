from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.list_rooms, name='list_rooms'),
    path('adicionar/', views.add_room, name='add_room'),
    path('editar/<int:id_room>/', views.edit_room, name='edit_room'),
    path('excluir/<int:id_room>/', views.delete_room, name='delete_room'),
]