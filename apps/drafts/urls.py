from django.urls import path
from . import views

app_name = 'drafts'

urlpatterns = [
    path('listar/', views.list_drafts, name='list_drafts'),
    path('adicionar/', views.add_draft, name='add_draft'),
    path('editar/<int:id_draft>/', views.edit_draft, name='edit_draft'),
    path('excluir/<int:id_draft>/', views.delete_draft, name='delete_draft'),
]