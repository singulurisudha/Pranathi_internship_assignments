from django.contrib import admin
from django.urls import path 
from library.views import BookStatusAPIView , StudentStatusAPIView

urlpatterns = [

    path('get/book/',BookStatusAPIView.as_view(),name='get_book'),
    path('get/book/<int:pk>/',BookStatusAPIView.as_view(),name='get_book'),
    path('put/book/<int:pk>/',BookStatusAPIView.as_view(),name='put_book'),
    path('delete/book/<int:pk>/',BookStatusAPIView.as_view(),name='delete_book'),
    path('post/book/',BookStatusAPIView.as_view(),name='post_book'),
    path('get/student/',StudentStatusAPIView.as_view(),name='get_student'),
    path('get/student/<int:pk>/',StudentStatusAPIView.as_view(),name='get_student'),
    path('post/student/',StudentStatusAPIView.as_view(),name='post_student'),
    path('put/student/<int:pk>/',StudentStatusAPIView.as_view(),name='put_student'),
    path('delete/student/<int:pk>/',StudentStatusAPIView.as_view(),name='delete_student'),
    
]