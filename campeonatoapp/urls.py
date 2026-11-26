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
    path('inscricoes/', include('registrations.urls', namespace='registrations')),
    path('fases/', include('stages.urls', namespace='stages')),
    path('partidas/', include('matches.urls', namespace='matches')),
    path('jogos/', include('games.urls', namespace='games')),
    path('drafts/', include('drafts.urls', namespace='drafts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)