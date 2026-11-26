from django.urls import path
from . import views

app_name = 'playerstats'

urlpatterns = [
    path('listar/', views.list_playerstats, name='list_playerstats'),
    path('adicionar/', views.add_playerstat, name='add_playerstat'),
    path('editar/<int:id_playerstat>/', views.edit_playerstat, name='edit_playerstat'),
    path('excluir/<int:id_playerstat>/', views.delete_playerstat, name='delete_playerstat'),
]