from django.urls import path
from . import views
 
app_name = 'champions'
 
urlpatterns = [
    path('adicionar/', views.add_champion, name='add_champion'),
    path('listar/', views.list_champions, name='list_champions'),
    path('editar/<int:id_champion>/', views.edit_champion, name='edit_champion'),
    path('excluir/<int:id_champion>/', views.delete_champion, name='delete_champion'),
]
