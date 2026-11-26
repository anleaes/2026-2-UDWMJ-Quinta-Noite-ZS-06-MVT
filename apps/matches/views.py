from django.shortcuts import render, get_object_or_404, redirect
from drafts.views import update_champion_rates
from .forms import MatchForm
from .models import Match
 
def add_match(request):
    template_name = 'matches/add_match.html'
    context = {}
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('matches:list_matches')
    form = MatchForm()
    context['form'] = form
    return render(request, template_name, context)
 
def list_matches(request):
    template_name = 'matches/list_matches.html'
    matches = Match.objects.filter()
    context = {
        'matches': matches
    }
    return render(request, template_name, context)
 
def edit_match(request, id_match):
    template_name = 'matches/add_match.html'
    context ={}
    match = get_object_or_404(Match, id=id_match)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('matches:list_matches')
    form = MatchForm(instance=match)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_match(request, id_match):
    match = Match.objects.get(id=id_match)
    match.delete()
    return redirect('matches:list_matches')

def count_wins(match):
    wins_a = 0
    wins_b = 0
    for game in match.games.all():
        if game.winner == match.team_a:
            wins_a += 1
        elif game.winner == match.team_b:
            wins_b += 1
    return wins_a, wins_b

def view_match(request, id_match):
    template_name = 'matches/view_match.html'
    match = get_object_or_404(Match, id=id_match)
    wins_a, wins_b = count_wins(match)
    context = {
        'match': match,
        'games': match.games.all(),
        'wins_a': wins_a,
        'wins_b': wins_b,
    }
    return render(request, template_name, context)

def finish_match(request, id_match):
    match = get_object_or_404(Match, id=id_match)
    wins_a, wins_b = count_wins(match)
    needed = match.best_of // 2 + 1
    if wins_a >= needed:
        match.winner = match.team_a
        match.status = 'FIN'
    elif wins_b >= needed:
        match.winner = match.team_b
        match.status = 'FIN'
    elif wins_a + wins_b > 0:
        match.winner = None
        match.status = 'RUN'
    match.save()
    update_champion_rates()
    return redirect('matches:view_match', id_match=match.id)