from django.urls import path
from . import views
 
app_name = 'memberships'
 
urlpatterns = [
    path('listar/', views.list_memberships, name='list_memberships'),
    path('adicionar/', views.add_membership, name='add_membership'),
    path('editar/<int:id_membership>/', views.edit_membership, name='edit_membership'),
    path('excluir/<int:id_membership>/', views.delete_membership, name='delete_membership'),
]
