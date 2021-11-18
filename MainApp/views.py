from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm
from django.utils.datastructures import MultiValueDictKeyError



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets,
    }
    return render(request, 'pages/view_snippets.html', context)


def single_snippet_page(request, pk):

    try:
        snippet = Snippet.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        'pagename': 'Страница сниппета',
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
            form.save()
            return redirect("snippets-list")
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippet_delete(request, pk):
    snippet = Snippet.objects.get(id=pk)
    snippet.delete()
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
        snippet.name = form_data["name"]
        snippet.code = form_data["code"]
        snippet.save()
        return redirect("snippets-list")


