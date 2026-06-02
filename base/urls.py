from django.urls  import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('read/<int:pk>',read,name='read'),
    path('news/', news_home, name='news_home'),
    path('news/<int:pk>/',news_read, name='news_read'),
    path('events/',event_home, name='event_home'),
    path('events/<int:pk>/',event_read, name='event_read'),
    path('sports/',sports_home, name='sports_home'),
    path('sports/<int:pk>/',sports_read, name='sports_read'),

]