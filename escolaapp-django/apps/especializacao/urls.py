from django.urls import path
from . import views

app_name = 'especializacao'

urlpatterns = [
    path('', views.list_especializacoes, name='list_especializacoes'),
    path('adicionar/', views.add_especializacao, name='add_especializacao'),
    path('editar/<int:id_especializacao>/', views.edit_especializacao, name='edit_especializacao'),
    path('excluir/<int:id_especializacao>/', views.delete_especializacao, name='delete_especializacao'),
]