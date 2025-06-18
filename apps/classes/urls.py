from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.list_classes, name='list_classes'),
    path('adicionar/', views.add_class, name='add_class'),
    path('editar/<int:id_class>/', views.edit_class, name='edit_class'),
    path('excluir/<int:id_class>/', views.delete_class, name='delete_class'),
]
