from django.shortcuts import render
# from django.http import HttpResponse
# from app_two.models import User
from app_two.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request, 'app_two/index.html')


def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'app_two/users.html', {'form': form})


def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'app_two/help.html', context=helpdict)
