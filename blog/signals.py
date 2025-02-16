import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Post
from .utils import generate_wordcloud

@receiver(post_save, sender=Post)
def create_wordcloud(sender, instance, created, **kwargs):
    if created or not instance.wordcloud_image:
        # ワードクラウド画像を保存するパス
        output_path = os.path.join(
            settings.MEDIA_ROOT,
            'wordclouds',
            f'post_{instance.pk}_wordcloud.png'
        )
        # ワードクラウドの生成
        generate_wordcloud(instance.content, output_path)

        # 生成した画像をモデルに保存
        instance.wordcloud_image = f'wordclouds/post_{instance.pk}_wordcloud.png'
        instance.save()
