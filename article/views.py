from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken

from .models import Article
from .serializers import ArticleSerializer


def validate_jwt(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
        1]
    try:
        AccessToken(token)
        return True
    except InvalidToken:
        return False


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def manage_articles(request, article_id=None):
    is_valid_jwt = validate_jwt(request)
    if not is_valid_jwt:
        raise AuthenticationFailed('Invalid JWT')

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
            return Response({'message': '文章已成功建立'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                article.delete()
                return Response({'message': '文章已成功刪除'}, status=status.HTTP_200_OK)
            except Article.DoesNotExist:
                return Response({'error': '找不到指定的文章'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PATCH':
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                serializer = ArticleSerializer(
                    article, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': '文章已成功修改'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Article.DoesNotExist:
                return Response({'error': '找不到指定的文章'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': '缺少文章ID'}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'error': '其他錯誤'}, status=500)
