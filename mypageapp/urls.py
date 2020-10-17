from django.urls import path
from . import views

urlpatterns = [
    path('post_search.html', views.post_search, name = 'post_search'),
    path('post_search_detail.html', views.post_search_detail, name='post_search_detail'),
    path('timeline', views.timeline, name='timeline'),

    path('mypage', views.mypage, name="mypage"),
    path('post_reservation.html', views.post_reservation, name="post_reservation"),
    path('post_reserve_look.html', views.post_reserve_look, name="post_reserve_look"),
    path('post_reserve_look_detail', views.post_reserve_look_detail, name="post_reserve_look_detail"),
]