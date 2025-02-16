from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def chat_list(request):
    messages = ChatMessage.objects.order_by('-created_at')[:50]  # 最新50件
    messages_data = [
        {
            'user': msg.user.username,  # ユーザー名
            'content': msg.content,    # メッセージ内容
            'created_at': msg.created_at.strftime('%Y-%m-%d %H:%M:%S')  # 日時
        }
        for msg in messages
    ]
    return JsonResponse(messages_data, safe=False)  # JSON形式で返す

@login_required
@csrf_exempt
def post_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # JSONデータをパース
            content = data.get('content')
            if content:
                message = ChatMessage.objects.create(user=request.user, content=content)
                return JsonResponse({
                    'status': 'success',
                    'message': {
                        'user': message.user.username,
                        'content': message.content,
                        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    }
                })
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def get_messages(request):
    """最新のチャットメッセージを取得して返すビュー"""
    messages = ChatMessage.objects.order_by('-created_at')[:50]  # 最新50件
    messages_data = [
        {
            'user': message.user.username,
            'content': message.content,
            'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for message in messages
    ]
    return JsonResponse(messages_data, safe=False)  # JSON形式で返す