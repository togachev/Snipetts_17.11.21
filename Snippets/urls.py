from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views


urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippet/page/<int:pk>', views.single_snippet_page, name="snippet-page"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippets/my', views.snippet_my, name="snippets-my"),
    path('snippet/delete/<int:pk>', views.snippet_delete, name="snippet-delete"),
    path('snippet/edit/<int:pk>', views.snippet_edit, name="snippet-edit"),
    path('search', views.search_snippet, name='search-snippet'),
    path('auth/login', views.login_page, name="login"),
    path('auth/logout', views.logout, name="logout"),
    path('auth/register', views.register, name="register"),
    path('errors', views.errors_page, name="errors-page"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)