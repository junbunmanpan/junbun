# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('generate_wordcloud/', views.generate_wordcloud, name='generate_wordcloud'), 
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('guidelines/', views.guidelines, name='guidelines'),  # ガイドラインページ
    path('contact/', views.contact, name='contact'),  # 問い合わせページ
    path('about/', views.about, name='about'),
    path('guidelines/', views.guidelines, name='guidelines'),
]
