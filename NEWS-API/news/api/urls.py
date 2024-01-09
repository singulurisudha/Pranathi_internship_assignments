from django.urls import path
from news.api.views import article_list_create_api_view , article_detail_api_view
from django.urls import path
from news.api.views import ArticleListCreateApiView , ArticleDetailView , JournalistListCreateAPIView

urlpatterns =[
    path("articles/",article_list_create_api_view,name="article-list"),
    path("articles/<int:pk>/",article_detail_api_view,name="article-detail"),
    path("articles/",ArticleListCreateApiView.as_view(),name="article-list"),
    path("articles/<int:pk>/",ArticleDetailView.as_view(),name="article-detail"),
    path("journalists/",JournalistListCreateAPIView.as_view(),name="journalists-list")
]