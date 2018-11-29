from rest_framework import serializers
from .models import Favourite, Comments
from . import views


class FavouriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favourite
        fields = ('user_uuid', 'article')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comments
        fields = ('user_uuid', 'comment')
