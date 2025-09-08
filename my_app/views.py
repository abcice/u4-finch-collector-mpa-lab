
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chicken
from django.views.generic import ListView, DetailView # add these 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import EscapeAttemptForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404



# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')
# views.py
@login_required
def chicken_index(request):
    chickens = Chicken.objects.filter(user=request.user)
    return render(request, 'chickens/index.html', {'chickens': chickens})
# views.py

@login_required
def chicken_detail(request, chicken_id):
    chicken = Chicken.objects.get(id=chicken_id)
    escape_form = EscapeAttemptForm()
    return render(request, 'chickens/detail.html', {
        'chicken': chicken,
        'escape_form': escape_form
    })

# main-app/views.py

class ChickenCreate(LoginRequiredMixin, CreateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ChickenUpdate(LoginRequiredMixin, UpdateView):
    model = Chicken
    # Let's disallow the renaming of a Chicken by excluding the name field!
    fields = ['breed', 'description', 'age']

class ChickenDelete(LoginRequiredMixin, DeleteView):
    model = Chicken
    success_url = '/chickens/'

@login_required
def add_escape(request, chicken_id):
    chicken = get_object_or_404(Chicken, id=chicken_id)
    if request.method == 'POST':
        form = EscapeAttemptForm(request.POST)
        if form.is_valid():
            new_escape = form.save(commit=False)
            new_escape.chicken = chicken
            new_escape.save()
    return redirect('chicken-detail', chicken_id=chicken_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chicken-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)