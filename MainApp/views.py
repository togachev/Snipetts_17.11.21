from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.db.models import Q
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'Главная страница'}
    return render(request, 'pages/index.html', context)

def snippets_page(request):
    if request.user.is_superuser:
        snippets = Snippet.objects.all()
    else:
        snippets = Snippet.objects.filter(public=True)
    context = {
        'pagename': 'Список сниппетов',
        "snippets": snippets,
    }
    return render(request, 'pages/view_snippets.html', context)

def snippet_my(request):
    user_snippets = Snippet.objects.filter(user=request.user)
    context = {
        'pagename': 'Мои сниппеты',
        "snippets": user_snippets,
    }
    return render(request, 'pages/view_snippets.html', context)

def single_snippet_page(request, pk):
    try:
        snippet = Snippet.objects.get(id=pk)
    except ObjectDoesNotExist:
        raise Http404("Сниппет не найден..")
    context = {
        'pagename': 'Сниппет',
        'name': 'Название',
        'lang': 'Язык',
        'creation_date': 'Создан',
        'update_date': 'Обновлен',
        'user': 'Пользователь',
        'public': 'Доступ',
        "snippet": snippet,
        "type": "view"
    }
    return render(request, 'pages/snippet_page.html', context)

def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            else:
                # return redirect("errors-page")
                context = {
                    'pagename': 'Результат запроса',
                    'result': 'В операции отказано',
                }
                return render(request, 'pages/errors.html', context)
            return redirect("snippets-list")
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippet_delete(request, pk):
    snippet = Snippet.objects.get(id=pk)
    if snippet.user == request.user or request.user.is_superuser:
        snippet.delete()
    else:
        return redirect("errors-page")
    return redirect("snippets-list")


def snippet_edit(request, pk):
    try:
        snippet = Snippet.objects.get(id=pk)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "GET":
        context = {
            'pagename': 'Редактировать сниппет',
            "snippet": snippet,
            "type": 'edit'
        }
        return render(request, 'pages/snippet_page.html', context)

    if request.method == "POST":

        form_data = request.POST
        public = form_data.get("public") == 'on'
        snippet.name = form_data["name"]
        snippet.lang = form_data["lang"]
        snippet.code = form_data["code"]
        snippet.public = public
        if snippet.user == request.user or request.user.is_superuser:
            snippet.user = request.user
            snippet.save()
        else:
            return redirect("errors-page")
        return redirect("snippets-list")

def search_snippet(request):
    id = request.GET.get('result')
    if not id:
        context = {
            'pagename': 'Результат поиска',
            'result':'Снипет не найден',
        }
        return render(request, 'pages/index.html', context)
    try:
        # полное совпадение
        snippet = Snippet.objects.filter(Q(id__iexact=id))
        # если результат содержит часть
        # snippet = Snippet.objects.filter(Q(id__icontains=id))
    except ObjectDoesNotExist:
        snippet = None
    context = {
        'pagename': 'Результат поиска',
        "snippets": snippet,
        'result': 'Снипет не найден',
    }
    return render(request, 'pages/index.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            context = {
                'pagename': 'Главная страница',
                'result': 'Неверный логин или пароль'
            }
            return render(request, 'pages/index.html', context)

    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')

def errors_page(request):
    context = {
        'pagename': 'Результат запроса',
        'result': 'В операции отказано',
    }
    return render(request, 'pages/errors.html', context)

def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        context = {
            'pagename': 'Регистрация пользователя',
            'form': form
        }
        return render(request, 'pages/register.html', context)
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'pagename': 'Регистрация пользователя',
            'form': form
        }
        return render(request, 'pages/register.html', context)