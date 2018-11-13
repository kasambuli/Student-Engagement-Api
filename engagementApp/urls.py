from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    url(r'articles/', views.ArticleList.as_view()),
    url(r'article/(?P<pk>\d+)/', views.ArticleDetail.as_view()),
    url(r'users/', views.UserList.as_view()),
    url(r'user/(?P<pk>\d+)/', views.UserDetail.as_view()),
]
urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls')),
]
