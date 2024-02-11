from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('news/', category_page, name='news'),
    path('news/<str:tag>', category_page, name='tag_news'),
    path('contact/', contact_page, name='contact'),
    path('article/<str:slug>', singe_page, name='detail'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('account/', account_page, name='account'),
]
