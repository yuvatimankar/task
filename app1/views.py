from django.shortcuts import render

# Create your views here.
from .models import Login
from .forms import LoginForm

def create_view(request):
    context = {}

    form=LoginForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,"create_view.html",context)