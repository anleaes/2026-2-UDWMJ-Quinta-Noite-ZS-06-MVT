from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from registrations.models import Registration
from stages.models import Stage
from matches.models import Match
from .forms import TournamentForm
from .models import Tournament

@login_required(login_url='/contas/login/')
def add_tournament(request):
    template_name = 'tournaments/add_tournament.html'
    context = {}
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tournaments:list_tournaments')
    form = TournamentForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tournaments(request):
    template_name = 'tournaments/list_tournaments.html'
    tournaments = Tournament.objects.filter()
    context = {
        'tournaments': tournaments
    }
    return render(request, template_name, context)
 
def edit_tournament(request, id_tournament):
    template_name = 'tournaments/add_tournament.html'
    context ={}
    tournament = get_object_or_404(Tournament, id=id_tournament)
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES, instance=tournament)
        if form.is_valid():
            form.save()
            return redirect('tournaments:list_tournaments')
    form = TournamentForm(instance=tournament)
    context['form'] = form
    return render(request, template_name, context)

def delete_tournament(request, id_tournament):
    tournament = Tournament.objects.get(id=id_tournament)
    tournament.delete()
    return redirect('tournaments:list_tournaments')

def standings(request, id_tournament):
    template_name = 'tournaments/standings.html'
    tournament = get_object_or_404(Tournament, id=id_tournament)
    table = []
    registrations = Registration.objects.filter(tournament=tournament, status='CONF')
    for registration in registrations:
        wins = 0
        losses = 0
        for stage in Stage.objects.filter(tournament=tournament):
            for match in Match.objects.filter(stage=stage, status='FIN'):
                if match.winner == registration.team:
                    wins += 1
                elif match.team_a == registration.team or match.team_b == registration.team:
                    losses += 1
        table.append({'team': registration.team, 'wins': wins, 'losses': losses})
    table = sorted(table, key=lambda row: row['wins'], reverse=True)
    context = {
        'tournament': tournament,
        'table': table,
    }
    return render(request, template_name, context)