from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('adicionar/', views.add_student, name='add_student'),
    path('editar/<int:id_student>/', views.edit_student, name='edit_student'),
    path('excluir/<int:id_student>/', views.delete_student, name='delete_student'),
]