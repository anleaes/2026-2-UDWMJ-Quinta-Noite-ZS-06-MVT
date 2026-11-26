from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlayerGameStatForm
from .models import PlayerGameStat

def add_playerstat(request):
    template_name = 'playerstats/add_playerstat.html'
    context = {}
    if request.method == 'POST':
        form = PlayerGameStatForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('playerstats:list_playerstats')
    form = PlayerGameStatForm()
    context['form'] = form
    return render(request, template_name, context)
 
def list_playerstats(request):
    template_name = 'playerstats/list_playerstats.html'
    playerstats = PlayerGameStat.objects.filter()
    context = {
        'playerstats': playerstats
    }
    return render(request, template_name, context)
 
def edit_playerstat(request, id_playerstat):
    template_name = 'playerstats/add_playerstat.html'
    context ={}
    playerstat = get_object_or_404(PlayerGameStat, id=id_playerstat)
    if request.method == 'POST':
        form = PlayerGameStatForm(request.POST, instance=playerstat)
        if form.is_valid():
            form.save()
            return redirect('playerstats:list_playerstats')
    form = PlayerGameStatForm(instance=playerstat)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_playerstat(request, id_playerstat):
    playerstat = PlayerGameStat.objects.get(id=id_playerstat)
    playerstat.delete()
    return redirect('playerstats:list_playerstats')
