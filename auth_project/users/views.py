from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView

from .forms import Profiles

menu = [{'title': 'О сайте', "url_name": 'about'},
        {'title': "Добавить файлы", "url_name": 'add'},
        {'title': "Обратная связь", "url_name": 'contact'},
        {'title': "Войти", "url_name": 'login'}
        ]


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def homePageView(request):
    return HttpResponse('Hello, World!')


def profiles(request):
    if request.POST:
        form = Profiles(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data['path_file'])
            arh_name = form.cleaned_data['path_file']
            form.save()

            return HttpResponseRedirect("/")
    else:
        form = Profiles

    return render(request, 'users/profile.html',
                  {'form': form, 'menu': menu, 'title': 'Добавление файлов'})  # изменение данных в БД

