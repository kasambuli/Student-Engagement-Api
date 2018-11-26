from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser+
# from django.http import Http404
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics
from .models import Articles
from .serializer import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

 #this is the one for getting all the articles. So idealy, we get the objects from the model class then serialize them and return as Json data 

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })


class ArticleList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an article instance.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly, )
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleHighlight(generics.GenericAPIView):
    queryset=Articles.objects.all()
    render_classes=(renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
