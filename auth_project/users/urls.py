from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', views.SignUpView.as_view(), name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profiles, name='profile'),
    # path('orders/', order_add, name="order_add"),  # форма добавления заказа

]