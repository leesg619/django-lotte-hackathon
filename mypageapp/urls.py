from django.urls import path
from . import views

urlpatterns = [
    path('post_search/', views.post_search, name = 'post_search'),
    path('post_search_detail/', views.post_search_detail, name='post_search_detail'),
    path('timeline/', views.timeline, name='timeline'),
]