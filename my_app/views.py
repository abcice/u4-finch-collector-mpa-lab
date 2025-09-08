
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chicken
from django.views.generic import ListView, DetailView # add these 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import EscapeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
# views.py

def chicken_index(request):
    chickens = Chicken.objects.all() 
    return render(request, 'chickens/index.html', {'chickens': chickens})
# views.py

def chicken_detail(request, chicken_id):
    chicken = Chicken.objects.get(id=chicken_id)
    return render(request, 'chickens/detail.html', {'chicken': chicken})

# main-app/views.py

class ChickenCreate(CreateView):
    model = Chicken
    fields = '__all__'

class ChickenCreate(CreateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']

class ChickenUpdate(UpdateView):
    model = Chicken
    # Let's disallow the renaming of a Chicken by excluding the name field!
    fields = ['breed', 'description', 'age']

class ChickenDelete(DeleteView):
    model = Chicken
    success_url = '/chickens/'

# @login_required
def add_escape(request, chicken_id):
    form = EscapeForm(request.POST)
    if form.is_valid():
        new_escape = form.save(commit=False)
        new_escape.chicken_id = chicken_id
        new_escape.save()
    return redirect('chicken-detail', chicken_id=chicken_id)