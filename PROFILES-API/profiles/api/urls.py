from django.urls import path , include
from profiles.api.views import ProfileList

urlpatterns =[
    path("profiles/",ProfileList.as_view(),name='profile-list'),
    path('accounts/', include('allauth.urls')),
]

    