---
layout: post
title: "[python] Django REST framework에서의 소켓 통신(Socket communication) 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 강력한 웹 프레임워크이지만, 때로는 실시간 통신을 위한 소켓 통신이 필요할 수 있습니다. 이 글에서는 Django REST framework에서 소켓 통신을 구현하는 방법에 대해 알아보겠습니다.

## 소켓 라이브러리 설치하기

먼저, 소켓 통신을 구현하기 위해 `SocketIO`라이브러리를 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다.

```python
pip install django-socketio
```

## Django 설정 변경하기

Django의 `settings.py` 파일에서 다음과 같은 설정을 추가해야 합니다.

```python
INSTALLED_APPS = [
    ...
    'socketio'
]

MIDDLEWARE = [
    ...
    'socketio.contrib.django.middleware.SocketIOMiddleware'
]

# 소켓 관련 설정
SOCKETIO_ASYNC_MODE = 'threading'
```

## 소켓 통신 구현하기

Django REST framework와 소켓 통신을 함께 사용하기 위해서는 뷰(view)에서 소켓 통신을 처리해야 합니다. 다음은 간단한 예제 코드입니다.

```python
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin
from django_socketio import events

class MyNamespace(BaseNamespace, BroadcastMixin):
    def __init__(self, *args, **kwargs):
        super(MyNamespace, self).__init__(*args, **kwargs)
    
    def on_connect(self):
        print('소켓 연결됨')
        self.emit('connected', {'data': '소켓 연결됨'})
    
    def on_disconnect(self):
        print('소켓 연결 해제됨')
        self.emit('disconnected', {'data': '소켓 연결 해제됨'})
        
@events.on_message(namespace='/my_namespace')
def message(request, socket, context, message):
    print('메시지 수신:', message)
    socket.emit('message_received', {'message': message['message']})

def my_view(request):
    return render(request, 'my_template.html')
```

위 코드에서 `MyNamespace`는 소켓 이벤트를 처리하는 데에 사용됩니다. `on_connect`와 `on_disconnect`는 소켓 연결 및 연결 해제에 대한 처리를 담당합니다. `message`는 메시지를 수신하는 이벤트입니다.

뷰 함수 `my_view`에서는 소켓 통신을 사용할 HTML 템플릿을 렌더링합니다.

## 클라이언트 측 구현

마지막으로, 클라이언트 측에서도 소켓 통신을 처리해야 합니다. 일반적으로 JavaScript를 사용하여 클라이언트 소켓 코드를 작성합니다. 다음은 간단한 예제 코드입니다.

```javascript
// 소켓 연결
var socket = io.connect('http://localhost:8000/my_namespace');

// 연결 이벤트 리스너
socket.on('connect', function() {
    console.log('소켓 연결됨');
});

// 연결 해제 이벤트 리스너
socket.on('disconnect', function() {
    console.log('소켓 연결 해제됨');
});

// 메시지 수신 이벤트 리스너
socket.on('message_received', function(data) {
    console.log('메시지 수신:', data.message);
});
```

위 코드에서 `io.connect`는 서버의 소켓 연결 주소를 지정합니다. `connect`와 `disconnect` 이벤트 리스너는 각각 소켓 연결과 연결 해제에 대한 처리를 담당합니다. `message_received` 이벤트 리스너는 서버로부터 메시지를 수신할 때 동작합니다.

이제 Django REST framework에서 소켓 통신을 구현하는 방법에 대해 알게 되었습니다. 소켓 통신을 사용하면 실시간으로 데이터를 전송하고 처리할 수 있어서 웹 애플리케이션의 사용자 경험을 향상시킬 수 있습니다.

참고 자료:
- [Django REST framework 공식 문서](https://www.django-rest-framework.org/)
- [django-socketio 도큐먼트](https://github.com/stephenmcd/django-socketio)