from rest_framework import serializers
from .models import Articles
from django.contrib.auth.models import User
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields='__all__'
        owner = serializers.ReadOnlyField(source='owner.username'),

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())
    class Meta:
        model=User
        fields = ('id','username','articles')
