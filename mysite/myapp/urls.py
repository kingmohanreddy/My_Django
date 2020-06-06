from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_request, name='login'),
    path('newUser/', views.new_user, name='new_user'),
    path('resetPassword/', views.reset_pass, name='reset_pass'),
]
