from django.urls import path
from . import views
 
app_name = 'stages'
 
urlpatterns = [
    path('listar/', views.list_stages, name='list_stages'),
    path('adicionar/', views.add_stage, name='add_stage'),
    path('editar/<int:id_stage>/', views.edit_stage, name='edit_stage'),
    path('excluir/<int:id_stage>/', views.delete_stage, name='delete_stage'),
]
