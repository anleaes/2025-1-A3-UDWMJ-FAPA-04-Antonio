from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('', views.list_enrollments, name='list_enrollments'),
    path('adicionar/', views.add_enrollment, name='add_enrollment'),
    path('editar/<int:id_enrollment>/', views.edit_enrollment, name='edit_enrollment'),
    path('excluir/<int:id_enrollment>/', views.delete_enrollment, name='delete_enrollment'),
]