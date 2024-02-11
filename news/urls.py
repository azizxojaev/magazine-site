from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('news/', category_page, name='news'),
    path('contact/', contact_page, name='contact'),
    path('news/detail', singe_page, name='detail')
]
