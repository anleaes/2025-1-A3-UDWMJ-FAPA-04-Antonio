from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.list_teachers, name='list_teachers'),
    path('adicionar/', views.add_teacher, name='add_teacher'),
    path('editar/<int:id_teacher>/', views.edit_teacher, name='edit_teacher'),
    path('excluir/<int:id_teacher>/', views.delete_teacher, name='delete_teacher'),
]