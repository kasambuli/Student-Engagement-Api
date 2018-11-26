from rest_framework import serializers
from .models import Articles
from django.contrib.auth.models import User
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username'),
    highlight  =serializers.HyperlinkedIdentityField(view_name='article-highlight', format='html')
    class Meta:
        model = Articles
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'Content','category','author')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-highlight', read_only=True)
    class Meta:
        model=User
        fields = ('url','id','username','articles')
