from django.contrib import admin
from django.urls import path 
from accounts.views import UserRegistrationView , UserLoginView , UserProfileView , UserChangePasswordView , SendPasswordResetEmailView , UserPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('send_password_reset_email/',SendPasswordResetEmailView.as_view(),name='send_password_reset_email'),
    path('reset_password/<uid>/<token>/',UserPasswordResetView.as_view(),name='resetpassword'),
]