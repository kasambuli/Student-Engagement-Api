from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import SingleFavourite
#create a router and register our viewsets with it
router = DefaultRouter()

router.register(r'favourites', views.FavouriteViewSet),
router.register(r'comments', views.CommentViewSet)
# router.register(r'search', views.SingleFavouriteViewSet)

#The API URLs are now determined automatically by the router
urlpatterns = [
    url(r'', include(router.urls)),
    url('^search-by-uuid/(?P<user_uuid>.+)/$', SingleFavourite.as_view()),
]
