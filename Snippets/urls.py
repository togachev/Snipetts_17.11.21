from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippet/page/<int:id>', views.single_snippet_page, name="snippet-page"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippet/delete/<int:id>', views.snippet_delete, name="snippet-delete"),
    path('snippet/edit/<int:id>', views.snippet_edit, name="snippet-edit"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)