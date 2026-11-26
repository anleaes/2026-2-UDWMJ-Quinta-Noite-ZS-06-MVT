from django.shortcuts import render, get_object_or_404, redirect
from .forms import DraftForm
from .models import Draft
from champions.models import Champion

def add_draft(request):
    template_name = 'drafts/add_draft.html'
    context = {}
    if request.method == 'POST':
        form = DraftForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            #  chama a funcao para fazer a atualizacao automatica dos pickrates e banrater
            update_champion_rates()
            return redirect('drafts:list_drafts')
    form = DraftForm()
    context['form'] = form
    return render(request, template_name, context)

def list_drafts(request):
    template_name = 'drafts/list_drafts.html'
    drafts = Draft.objects.prefetch_related('blue_picks', 'red_picks', 'blue_bans', 'red_bans')
    context = {
        'drafts': drafts
    }
    return render(request, template_name, context)

def edit_draft(request, id_draft):
    template_name = 'drafts/add_draft.html'
    context ={}
    draft = get_object_or_404(Draft, id=id_draft)
    if request.method == 'POST':
        form = DraftForm(request.POST, instance=draft)
        if form.is_valid():
            form.save()
            #  chama a funcao para fazer a atualizacao automatica dos pickrates e banrater
            update_champion_rates()
            return redirect('drafts:list_drafts')
    form = DraftForm(instance=draft)
    context['form'] = form
    return render(request, template_name, context)

def delete_draft(request, id_draft):
    draft = Draft.objects.get(id=id_draft)
    draft.delete()
    #  chama a funcao para fazer a atualizacao automatica dos pickrates e banrater
    update_champion_rates()
    return redirect('drafts:list_drafts')

# funcao que faz a atualizacao automatica dos pickrates e banrates
def update_champion_rates():
    # quantidade total de drafts
    total = len(Draft.objects.all())
    # para cada campeao
    for champion in Champion.objects.all():
        # quantos drafts o campeao foi pickado e quantos drafts ele foi banido
        picks = len(Draft.objects.filter(blue_picks=champion)) + len(Draft.objects.filter(red_picks=champion))
        bans = len(Draft.objects.filter(blue_bans=champion)) + len(Draft.objects.filter(red_bans=champion))
        # calculo de porcentagem desses picks e bans caso ele tenha aparecido em algum dos dois
        if total > 0:
            champion.pick_rate = round(picks * 100 / total, 2)
            champion.ban_rate = round(bans * 100 / total, 2)
        else:
            champion.pick_rate = 0.0
            champion.ban_rate = 0.0
        champion.save()