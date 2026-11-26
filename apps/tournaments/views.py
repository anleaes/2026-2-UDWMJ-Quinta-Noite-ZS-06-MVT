from django.shortcuts import render, get_object_or_404, redirect
from .forms import TournamentForm
from .models import Tournament

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