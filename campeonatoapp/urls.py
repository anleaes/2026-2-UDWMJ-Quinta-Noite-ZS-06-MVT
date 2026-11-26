from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('campeoes/', include('champions.urls', namespace='champions')),
    path('jogadores/', include('players.urls', namespace='players')),
    path('times/', include('teams.urls', namespace='teams')),
    path('tecnicos/', include('coaches.urls', namespace='coaches')),
    path('participacoes/', include('memberships.urls', namespace='memberships')),
    path('torneios/', include('tournaments.urls', namespace='tournaments')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)