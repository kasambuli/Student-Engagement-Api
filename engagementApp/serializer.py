from rest_framework import serializers
from .models import Articles
from django.contrib.auth.models import User
from . import views 

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username'),
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='users', format='html')
    class Meta:
        model = Articles
        fields = ('url', 'id', 'owner',
                  'title', 'Content','category','author')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # articles = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='users', read_only=True)
    class Meta:
        model=User
        fields = ('url','id','username','articles')
