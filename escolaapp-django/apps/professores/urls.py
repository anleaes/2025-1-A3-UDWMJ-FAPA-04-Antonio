from django.urls import path
from . import views

app_name = 'professores'

urlpatterns = [
    path('', views.list_professores, name='list_professores'),
    path('adicionar/', views.add_professor, name='add_professor'),
    path('editar/<int:id_professor>/', views.edit_professor, name='edit_professor'),
    path('excluir/<int:id_professor>/', views.delete_professor, name='delete_professor'),
]