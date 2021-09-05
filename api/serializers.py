from rest_framework import fields, serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']