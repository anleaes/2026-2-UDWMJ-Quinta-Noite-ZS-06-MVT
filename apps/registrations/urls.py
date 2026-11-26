from django.urls import path
from . import views
 
app_name = 'registrations'
 
urlpatterns = [
    path('listar/', views.list_registrations, name='list_registrations'),
    path('adicionar/', views.add_registration, name='add_registration'),
    path('editar/<int:id_registration>/', views.edit_registration, name='edit_registration'),
    path('excluir/<int:id_registration>/', views.delete_registration, name='delete_registration'),
]