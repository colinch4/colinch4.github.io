---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 실시간 채팅 구현"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

실시간 채팅을 구현하기 위해 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용할 수 있습니다. 이 두 함수를 이용하여 채팅 메시지를 주기적으로 가져와 보여주는 기능을 구현할 수 있습니다.

## HTML 구조 작성하기

먼저, HTML 구조를 작성해야 합니다. 다음은 채팅 창과 입력 필드를 포함한 기본적인 HTML 구조입니다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>실시간 채팅</title>
    <script src="chat.js"></script>
</head>
<body>
    <div id="chat-messages"></div>
    <input type="text" id="message-input" />
    <button onclick="sendMessage()">전송</button>
</body>
</html>
```

## JavaScript 코드 작성하기

다음으로, JavaScript 코드를 작성하여 실시간 채팅을 구현해보겠습니다. 

```javascript
// 채팅 메시지를 가져와 화면에 보여주는 함수
function fetchChatMessages() {
    // 채팅 메시지를 가져오는 비동기 요청
    // 이 부분은 실제로 서버에서 채팅 메시지를 가져오는 로직으로 대체해야 합니다.
    var chatMessages = [
        "안녕하세요!",
        "어떻게 지내세요?",
        "좋은 하루 되세요!"
    ];

    var chatMessagesDiv = document.getElementById("chat-messages");

    // 이전에 보여준 메시지들을 모두 지우고, 새로운 메시지를 추가합니다.
    chatMessagesDiv.innerHTML = "";
    chatMessages.forEach(function(message) {
        var messageElement = document.createElement("p");
        messageElement.innerText = message;
        chatMessagesDiv.appendChild(messageElement);
    });
}

// 주기적으로 채팅 메시지를 가져와 화면에 보여주는 함수
function startFetchingChatMessages() {
    fetchChatMessages();
    setInterval(fetchChatMessages, 5000); // 5초마다 실행
}

// 메시지 전송 함수
function sendMessage() {
    var messageInput = document.getElementById("message-input");
    var message = messageInput.value;

    // 메시지를 서버로 보내는 로직이 있어야 합니다.
    // 이 예제에서는 단순히 로그에 출력하게 됩니다.
    console.log("메시지 전송:", message);

    messageInput.value = ""; // 입력 필드 비우기
}

// 채팅 메시지 가져오기 시작
startFetchingChatMessages();
```

## 서버 로직 구현하기

위 예제에서는 채팅 메시지를 서버에서 가져오는 로직이 없으므로, 실제 사용할 때는 서버 로직을 구현해야 합니다. 서버와 클라이언트 간의 통신을 위해 AJAX, WebSocket 등을 사용할 수 있습니다. 이 부분은 서버 환경과 사용하고자 하는 기술에 따라 다를 수 있으므로, 자세한 구현 방법은 해당 기술의 문서를 참조하시기 바랍니다.

## 결론

위 예제에서는 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용하여 실시간 채팅을 구현하는 방법을 알아보았습니다. 이를 기반으로 서버와 클라이언트 간의 통신을 구현하여 실제로 실시간 채팅을 구현해보세요.