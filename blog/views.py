from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm
import uuid
import os
from django.conf import settings
from .utils import generate_wordcloud  # ユーティリティをインポート
from .models import Announcement

# 新着投稿一覧を表示

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')  # 公開された投稿のみを取得
    for post in posts:
        # ワードクラウドを生成してURLを設定
        if not post.wordcloud_url:  # wordcloud_urlが未設定の場合
            post.wordcloud_url = generate_wordcloud(post.text, post.id)  # post.id を渡す
            post.save()  # 生成したURLを保存
    return render(request, 'blog/post_list.html', {'posts': posts})


# 投稿詳細ページ
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 指定された投稿を取得
    other_posts = Post.objects.filter(is_published=True).exclude(pk=pk).order_by('-created_at')[:5]  # 公開された他の投稿を取得
    return render(request, 'blog/post_detail.html', {'post': post, 'other_posts': other_posts})

# 新規投稿ページ
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            # 投稿IDを自動付与（UUIDを利用）
            post.unique_id = str(uuid.uuid4())[:8]  # 8文字のランダムIDを付与

            # ワードクラウド生成
            text = post.text
            wordcloud_url = generate_wordcloud(text)

            if wordcloud_url:
                post.wordcloud_url = wordcloud_url  # 生成したURLを投稿に保存
                post.save()

                messages.success(request, "投稿が完了しました！")
                return redirect("blog:post_list")  # ポストリストへリダイレクト
            else:
                messages.error(request, "ワードクラウドの生成に失敗しました。")
                post.save()

        else:
            messages.error(request, "投稿に失敗しました。")

    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})

# ワードクラウドを生成するユーティリティ関数
def generate_wordcloud(text, post_id):  # 引数を２つ取る
    from wordcloud import WordCloud
    import os

    if not text.strip():
        return None

        # settingsからフォントパスを取得
    font_path = settings.FONT_PATH
    # ファイル名の生成
    filename = f"wordcloud_{post_id}_{uuid.uuid4().hex}.png"
    filepath = os.path.join(settings.MEDIA_ROOT, "wordclouds", filename)

    # ワードクラウド生成
    wc = WordCloud(width=400, height=400, background_color="white", font_path=settings.FONT_PATH)
    wc.generate(text)
    wc.to_file(filepath)

    wordcloud_url = os.path.join(settings.MEDIA_URL, "wordclouds", filename)
    return wordcloud_url


def announcement_list(request):
    announcements = Announcement.objects.all()  # 例: 全てのお知らせを取得
    return render(request, 'blog/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)  # 特定のお知らせを取得
    return render(request, 'blog/announcement_detail.html', {'announcement': announcement})

def guidelines(request):
    return render(request, 'blog/guidelines.html')

def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')