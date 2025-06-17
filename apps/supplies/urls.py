from django.urls import path
from . import views

app_name = 'supplies'

urlpatterns = [
    path('', views.list_supplies, name='list_supplies'),
    path('adicionar/', views.add_supply, name='add_supply'),
    path('editar/<int:id_supply>/', views.edit_supply, name='edit_supply'),
    path('excluir/<int:id_supply>/', views.delete_supply, name='delete_supply'),
]