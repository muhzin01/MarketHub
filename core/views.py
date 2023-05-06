from django.shortcuts import render, redirect,get_object_or_404

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()
    # item = get_object_or_404(Item, pk=pk)

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
def catview(request,pk):
    # item = get_object_or_404(Item, name=category)
    related_items = Item.objects.filter(category=pk)
    return render(request, 'core/cat.html', {
        'items1': related_items
    })