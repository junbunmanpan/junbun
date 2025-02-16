from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('post_message/', views.post_message, name='post_message'),  # メッセージ投稿用
    path('get_messages/', views.get_messages, name='get_messages'),  # メッセージ取得用
]
