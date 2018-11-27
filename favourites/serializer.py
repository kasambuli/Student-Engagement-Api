from rest_framework import serializers
from .models import Favourite
from . import views


class FavouriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favourite
        fields = ('user_uuid', 'article')
