from django.shortcuts import render,get_object_or_404, redirect
from .forms import CoachForm
from .models import Coach

def add_coach(request):
    template_name = 'coaches/add_coach.html'
    context = {}
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('coaches:list_coaches')
    form = CoachForm()
    context['form'] = form
    return render(request, template_name, context)

def list_coaches(request):
    template_name = 'coaches/list_coaches.html'
    coaches = Coach.objects.filter()
    context = {
        'coaches': coaches
    }
    return render(request, template_name, context)
 
def edit_coach(request, id_coach):
    template_name = 'coaches/add_coach.html'
    context = {}
    coach = get_object_or_404(Coach, id=id_coach)
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coaches:list_coaches')
    form = CoachForm(instance=coach)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_coach(request, id_coach):
    coach = Coach.objects.get(id=id_coach)
    coach.delete()
    return redirect('coaches:list_coaches')

