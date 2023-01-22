from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # path('', views.SignUpView.as_view(), name='signup'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('signup/', views.SignUpView.as_view(), name='signup'),


]
