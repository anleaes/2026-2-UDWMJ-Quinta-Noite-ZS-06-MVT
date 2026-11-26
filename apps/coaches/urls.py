from django.urls import path
from . import views
 
app_name = 'coaches'
 
urlpatterns = [
    path('listar/', views.list_coaches, name='list_coaches'),
    path('adicionar/', views.add_coach, name='add_coach'),
    path('editar/<int:id_coach>/', views.edit_coach, name='edit_coach'),
    path('excluir/<int:id_coach>/', views.delete_coach, name='delete_coach'),
]
