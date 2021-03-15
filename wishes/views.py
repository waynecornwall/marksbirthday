from django.shortcuts import render, redirect, get_object_or_404
from .models import Wish
from .forms import WishForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


# @login_required
def index(request):
    """ Displays all wishes """
    if not request.user.is_authenticated:
        return redirect('users:login')
    # Grab all wishes from database
    wishes = Wish.objects.order_by('date_posted')
    user_wishes = Wish.objects.filter(sender=request.user).all()
    user_wish_count = len(user_wishes)
    # Render page
    context = {
        'wishes' : wishes,
        'user_wish_count' : user_wish_count,
        'user_wishes' : user_wishes
    }
    return render(request, 'wishes/index.html', context)


@login_required
def post_wish(request):
    """ Send Mark a birthday wish """
    # Display blank form
    if request.method != 'POST':
        form = WishForm()
    # Process filled out form
    else:
        form = WishForm(data=request.POST)
        if form.is_valid():
            new_wish = form.save(commit=False)
            new_wish.sender = request.user
            new_wish.save()
            return redirect('wishes:index')
    # Render page if form is blank or invalid
    context = {
        'form' : form
    }
    return render(request, 'wishes/post_wish.html', context)


@login_required
def edit_wish(request, wish_id):
    """ Edit your birthday wish """
    # Grad a specific wish from database
    wish = get_object_or_404(Wish, id=wish_id)
    if wish.sender != request.user:
        raise Http404
    # Display form pre-filled with data from wish object
    if request.method != 'POST':
        form = WishForm(instance=wish)
    # Process form with changes made
    else:
        form = WishForm(instance=wish, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('wishes:index')
    # Render page
    context = {
        'wish' : wish,
        'form' : form
    }
    return render(request, 'wishes/edit_wish.html', context)


@login_required
def delete_wish(request, wish_id):
    """ Delete your wish """
    # Grab specific wish from database
    wish = get_object_or_404(Wish, id=wish_id)
    if wish.sender != request.user:
        raise Http404
    # Delete wish if request method is post
    if request.method == 'POST':
        if wish.id == wish_id:
            wish.delete()
            return redirect('wishes:index')
    # Render page
    context = {
        'wish' : wish,
    }
    return render(request, 'wishes/delete_wish.html', context)



