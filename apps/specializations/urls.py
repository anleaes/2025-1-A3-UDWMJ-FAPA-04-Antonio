from django.urls import path
from . import views

app_name = 'specializations'

urlpatterns = [
    path('', views.list_specializations, name='list_specializations'),
    path('adicionar/', views.add_specialization, name='add_specialization'),
    path('editar/<int:id_specialization>/', views.edit_specialization, name='edit_specialization'),
    path('excluir/<int:id_specialization>/', views.delete_specialization, name='delete_specialization'),
]