from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser+
# from django.http import Http404
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework import mixins
# from rest_framework import generics
from .models import Articles
from .serializer import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

 #this is the one for getting all the articles. So idealy, we get the objects from the model class then serialize them and return as Json data 

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list and detail actons.
    """
    queryset= User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, update and destroy actions
    We also need a highlight action
    """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     article = self.get_object()
    #     return Response(article.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
