from django.shortcuts import render, get_object_or_404, redirect
from .forms import MembershipForm
from .models import Membership

 
def add_membership(request):
    template_name = 'memberships/add_membership.html'
    context = {}
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('memberships:list_memberships')
    form = MembershipForm()
    context['form'] = form
    return render(request, template_name, context)
 
def list_memberships(request):
    template_name = 'memberships/list_memberships.html'
    memberships = Membership.objects.filter()
    context = {
        'memberships': memberships
    }
    return render(request, template_name, context)
 
def edit_membership(request, id_membership):
    template_name = 'memberships/add_membership.html'
    context ={}
    membership = get_object_or_404(Membership, id=id_membership)
    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect('memberships:list_memberships')
    form = MembershipForm(instance=membership)
    context['form'] = form
    return render(request, template_name, context)
 
def delete_membership(request, id_membership):
    membership = Membership.objects.get(id=id_membership)
    membership.delete()
    return redirect('memberships:list_memberships')
