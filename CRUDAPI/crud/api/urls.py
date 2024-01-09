from django.urls import path
from crud.api.views import StudentAPIView

urlpatterns = [
    path('students/',StudentAPIView.as_view(),name='student-get-All'),
    path('students/<int:pk>/',StudentAPIView.as_view(),name='student-get-One'),
    path('students/<int:pk>/percentage/',StudentAPIView.as_view(),name='student-get-percentage'),
    path('students/create/',StudentAPIView.as_view(),name='student-api2'),
    path('students/<int:pk>/get/',StudentAPIView.as_view(),name='student-get'),
    path('students/<int:pk>/update/',StudentAPIView.as_view(),name='student-update'),
    path('students/<int:pk>/delete/',StudentAPIView.as_view(),name='student-delete')
]