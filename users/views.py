from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.sender = request.user
            new_user.save()
            login(request, new_user)
            return redirect('wishes:index')
    context = {
        'form' : form
    }
    return render(request, 'registration/register.html', context)
