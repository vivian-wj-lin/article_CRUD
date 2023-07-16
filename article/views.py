from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def manage_articles(request):
    if request.method == 'GET':
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

    return JsonResponse({'error': '現在只接受 GET 和 POST 請求'})
