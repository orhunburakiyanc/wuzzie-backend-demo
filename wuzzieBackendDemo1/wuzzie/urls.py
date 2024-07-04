from django.urls import path

from wuzzie import views
from wuzzie.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-view'),
    path('login/', views.LoginView.as_view(), name='login-view'),
    path('user', views.UserView.as_view(), name='user-view'),
    path('logout/', views.LogoutView.as_view(), name='logout-view'),
    # Add more paths as needed
]
