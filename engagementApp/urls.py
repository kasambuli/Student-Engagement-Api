from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^articles/', views.article_list),
    url(r'^articles/<int:pk>/', views.single_article),
]
