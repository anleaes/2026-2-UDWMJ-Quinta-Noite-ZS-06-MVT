from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm
from .models import Registration

def add_registration(request):
    template_name = 'registrations/add_registration.html'
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('registrations:list_registrations')
    form = RegistrationForm()
    context['form'] = form
    return render(request, template_name, context)

def list_registrations(request):
    template_name = 'registrations/list_registrations.html'
    registrations = Registration.objects.filter()
    context = {
        'registrations': registrations
    }
    return render(request, template_name, context)

def edit_registration(request, id_registration):
    template_name = 'registrations/add_registration.html'
    context ={}
    registration = get_object_or_404(Registration, id=id_registration)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registrations:list_registrations')
    form = RegistrationForm(instance=registration)
    context['form'] = form
    return render(request, template_name, context)

def delete_registration(request, id_registration):
    registration = Registration.objects.get(id=id_registration)
    registration.delete()
    return redirect('registrations:list_registrations')