from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import StageForm
from .models import Stage

@login_required(login_url='/contas/login/')
def add_stage(request):
    template_name = 'stages/add_stage.html'
    context = {}
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('stages:list_stages')
    form = StageForm()
    context['form'] = form
    return render(request, template_name, context)

def list_stages(request):
    template_name = 'stages/list_stages.html'
    stages = Stage.objects.filter()
    context = {
        'stages': stages
    }
    return render(request, template_name, context)

def edit_stage(request, id_stage):
    template_name = 'stages/add_stage.html'
    context ={}
    stage = get_object_or_404(Stage, id=id_stage)
    if request.method == 'POST':
        form = StageForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
            return redirect('stages:list_stages')
    form = StageForm(instance=stage)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_stage(request, id_stage):
    stage = Stage.objects.get(id=id_stage)
    stage.delete()
    return redirect('stages:list_stages')
