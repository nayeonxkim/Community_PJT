from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)