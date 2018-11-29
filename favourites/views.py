from rest_framework import viewsets
from .models import Favourite, Comments
from .serializer import FavouriteSerializer, CommentSerializer
from rest_framework import filters
from rest_framework import generics

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'favourites': reverse('favourites-list', request=request, format=format)
#     })
class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

# class SingleFavouriteViewSet(viewsets.ModelViewSet):
#     queryset = Favourite.objects.all()
#     serializer_class = FavouriteSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('user_uuid',)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class SingleFavourite(generics.ListAPIView):
    serializer_class = FavouriteSerializer


    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_uuid = self.kwargs['user_uuid']
        return Favourite.objects.filter(user_uuid=user_uuid)
