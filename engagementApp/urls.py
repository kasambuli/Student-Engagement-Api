from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    url(r'articles/', views.ArticleList.as_view(), name = 'article-list'),
    url(r'article/(?P<pk>\d+)/', views.ArticleDetail.as_view(), name = 'articles-detail'),
    url(r'users/', views.UserList.as_view(), name='user-list'),
    url(r'user/(?P<pk>\d+)/', views.UserDetail.as_view(), name='user-detail'),
    # url(r'', views.api_root),
    url(r'articles/(?P<pk>\d+)/highlight', views.ArticleHighlight.as_view(), name = 'article-highlight'),
]
urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls')),
]
