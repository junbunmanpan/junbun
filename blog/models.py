from django.db import models
from django.utils.timezone import now
import uuid

class Post(models.Model):
    unique_id = models.CharField(max_length=8, unique=True, editable=False, default=lambda: str(uuid.uuid4())[:8])
    text = models.TextField()
    wordcloud_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)  # 常に公開
    unique_id = models.CharField(max_length=255, unique=True, default=uuid.uuid4, editable=False)
    
class Announcement(models.Model):
    title = models.CharField(max_length=200)  # タイトル
    content = models.TextField()  # 本文
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時

    def __str__(self):
        return self.title

