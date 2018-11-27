from rest_framework import viewsets
from .models import Favourite
from .serializer import FavouriteSerializer


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'favourites': reverse('favourites-list', request=request, format=format)
#     })


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
