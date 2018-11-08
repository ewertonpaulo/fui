from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from event.models import Event

# Create your views here.

def index(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    events = paginator.get_page(page)
    context_dict = {'events': events}
    return render(request, 'home/index.html', context=context_dict)

def search(request):
    context_dict = {'nome_do_prato': "Pizza de Pepperoni"}
    return render(request, 'search/search.html', context=context_dict)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Wellcome')
    else:
        form = LoginForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context=context_dict)

def logout_user(request):
    logout(request)
    return redirect('logout')