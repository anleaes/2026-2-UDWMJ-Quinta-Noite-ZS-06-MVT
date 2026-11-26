from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ChampionForm
from .models import Champion
 
@login_required(login_url='/contas/login/')
def add_champion(request):
    template_name = 'champions/add_champion.html'
    context = {}
    if request.method == 'POST':
        form = ChampionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('champions:list_champions')
    form = ChampionForm()
    context['form'] = form
    return render(request, template_name, context)

def list_champions(request):
    template_name = 'champions/list_champions.html'
    champions = Champion.objects.filter()
    context = {
        'champions': champions
    }
    return render(request, template_name, context)

def edit_champion(request, id_champion):
    template_name = 'champions/add_champion.html'
    context ={}
    champion = get_object_or_404(Champion, id=id_champion)
    if request.method == 'POST':
        form = ChampionForm(request.POST, request.FILES, instance=champion)
        if form.is_valid():
            form.save()
            return redirect('champions:list_champions')
    form = ChampionForm(instance=champion)
    context['form'] = form
    return render(request, template_name, context)

def delete_champion(request, id_champion):
    champion = Champion.objects.get(id=id_champion)
    champion.delete()
    return redirect('champions:list_champions')
    