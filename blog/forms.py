from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'text', ]  # フォームに表示するフィールドを指定
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full h-64 p-3 border border-gray-300 rounded-lg focus:outline-none',
                'placeholder': '本文を入力してください。',
                'style': 'resize: none;',  # リサイズ機能を無効化
            }),
        }
