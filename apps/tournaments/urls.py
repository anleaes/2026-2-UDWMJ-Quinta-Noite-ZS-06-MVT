from django.urls import path
from . import views
 
app_name = 'tournaments'
 
urlpatterns = [
    path('listar/', views.list_tournaments, name='list_tournaments'),
    path('adicionar/', views.add_tournament, name='add_tournament'),
    path('editar/<int:id_tournament>/', views.edit_tournament, name='edit_tournament'),
    path('excluir/<int:id_tournament>/', views.delete_tournament, name='delete_tournament'),
]
