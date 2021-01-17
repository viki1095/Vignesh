from django.shortcuts import render
from .models import Register
from django.contrib import messages
from .forms import reg_forms


def simple_register(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('password') and request.POST.get('city') and request.POST.get('state') and request.POST.get('country'):
            saverec = Register()
            saverec.first_name = request.POST.get('first_name')
            saverec.last_name = request.POST.get('last_name')
            saverec.email = request.POST.get('email')
            saverec.phone = request.POST.get('phone')
            saverec.password = request.POST.get('password')
            saverec.city = request.POST.get('city')
            saverec.state = request.POST.get('state')
            saverec.country = request.POST.get('country')
            saverec.save()
            messages.success(request, 'Records saved successfully..!')
            return render(request, 'index.html')
    else:
            return render(request, 'index.html')

def lists(request):
    result = Register.objects.all()
    return render(request, 'list_view.html', {'Register': result})
def edits(request,id):
    editdata = Register.objects.get(id=id)
    return render(request, 'edit_view.html', {'Register': editdata})
def updates(request,id):
    updatedata=Register.objects.get(id=id)
    form = reg_forms(request.POST, instance=updatedata)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated Successfully..!')
        return render(request, 'edit_view.html', {'Register':updatedata})
def deletes(request, id):
    deletedata = Register.objects.get(id=id)
    deletedata.delete()
    result = Register.objects.all()
    return render(request, 'list_view.html', {'Register':result})