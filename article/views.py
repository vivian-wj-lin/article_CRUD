from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def manage_articles(request, article_id=None):
    if request.method == 'GET':
        if article_id:
            try:
                articles = Article.objects.get(id=article_id)
                serializer = ArticleSerializer(articles)
                return Response(serializer.data)
            except Article.DoesNotExist:
                return Response({'error': '找不到指定的文章'}, status=status.HTTP_404_NOT_FOUND)

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '文章已成功建立'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                article.delete()
                return Response({'message': '文章已成功刪除'})
            except Article.DoesNotExist:
                return Response({'error': '找不到指定的文章'}, status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({'error': '請求方法不支援'})
