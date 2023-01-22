from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('signup/', views.SignUpView.as_view(), name='signup'),


]
