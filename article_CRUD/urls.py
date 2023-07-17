
from django.contrib import admin
from django.urls import path
from article.views import manage_articles
from users.views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/articles/', manage_articles, name='manage_articles'),
    path('api/articles/<int:article_id>/',
         manage_articles, name='manage_article_detail'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/login/', LoginView.as_view(), name='login'),


]
