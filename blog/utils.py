import uuid
import os
from wordcloud import WordCloud
from django.conf import settings
import matplotlib.font_manager as fm

def generate_wordcloud(text):
    print("ワードクラウド生成処理を開始")  # デバッグ用

    if not text.strip():
        print("テキストが空です")  # デバッグ用
        return None

    filename = f"wordcloud_{uuid.uuid4().hex}.png"
    filepath = os.path.join(settings.MEDIA_ROOT, "wordclouds", filename)

    # メディアディレクトリを確認
    if not os.path.exists(settings.MEDIA_ROOT):
        print(f"MEDIA_ROOT が存在しないため作成: {settings.MEDIA_ROOT}")
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    print(f"ワードクラウド保存先: {filepath}")  # デバッグ用

    try:
        font_path = getattr(settings, "FONT_PATH", None)
        if not font_path:
            font_path = fm.findSystemFonts(fontpaths=None, fontext='ttf')[0]  # システムフォントの1つを使用
            print(f"フォントが見つからないためシステムフォントを使用: {font_path}")  # デバッグ用

        wc = WordCloud(width=400, height=400, background_color="white", font_path=font_path)
        wc.generate(text)
        wc.to_file(filepath)

        # 画像ファイルが本当に作成されたか確認
        if not os.path.exists(filepath):
            print(f"ワードクラウド画像が作成されませんでした: {filepath}")
            return None

        print(f"ワードクラウド保存成功: {filepath}")  # デバッグ用
    except Exception as e:
        print(f"ワードクラウド生成エラー: {e}")  # デバッグ用
        return None

    wordcloud_url = f"{settings.MEDIA_URL}wordclouds/{filename}"
    print(f"生成されたワードクラウドURL: {wordcloud_url}")  # デバッグ用
    return wordcloud_url
