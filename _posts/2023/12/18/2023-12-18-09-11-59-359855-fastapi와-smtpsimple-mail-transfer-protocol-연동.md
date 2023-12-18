---
layout: post
title: "[python] FastAPI와 SMTP(Simple Mail Transfer Protocol) 연동"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

FastAPI는 강력하고 빠르며, 현대적인 Python 웹 프레임워크로, 간단한 웹 서비스부터 복잡한 웹 애플리케이션까지 다양한 용도로 사용됩니다. 이제 FastAPI 서비스에서 이메일을 보내야 하는 경우를 가정해보겠습니다. 이 글에서는 FastAPI와 SMTP를 연동하여 이메일을 보내는 방법에 대해 알아보겠습니다.

## 필요한 라이브러리 설치

먼저 이메일을 보내기 위해 필요한 `smtplib` 라이브러리를 설치해야 합니다. 아래 명령을 사용하여 설치할 수 있습니다.

```python
pip install secure-smtplib
```

이제 FastAPI에서 SMTP 프로토콜을 사용하여 이메일을 보내기 위한 라이브러리를 설치했습니다.

## FastAPI 서비스 구현

이제 FastAPI 서비스에 이메일을 보내는 기능을 추가해보겠습니다. 먼저 다음과 같이 필요한 FastAPI 및 smtplib 라이브러리를 import 합니다.

```python
from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
```

이제 FastAPI의 `/send_email` 엔드포인트를 생성하고, 해당 엔드포인트에 POST 요청을 받으면 이메일을 보내는 기능을 구현할 수 있습니다. 아래는 간단한 예시 코드입니다.

```python
app = FastAPI()

@app.post("/send_email")
async def send_email(email: str, subject: str, content: str):
    from_email = "your_email@gmail.com"
    to_email = email

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    body = content
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "your_password")
    server.send_message(msg)
    server.quit()
    return {"message": "Email sent successfully"}
```

위 코드에서는 `send_email` POST 요청을 처리하고, 받은 `email`, `subject`, `content`를 사용하여 이메일을 구성하고 보냅니다.

## 보안 및 인증

SMTP 서버를 사용하여 이메일을 보내는 경우, 보안과 인증에 대한 고려가 필요합니다. 디지털 서명 및 보안을 유지하기 위해 SMTP over SSL 또는 TLS를 사용할 수 있습니다. 또한, SMTP 서버에 로그인하여 인증하는 방법도 강화할 필요가 있습니다.

이제 FastAPI와 SMTP(Simple Mail Transfer Protocol)를 연동하여 이메일을 보내는 방법에 대한 기본적인 내용을 살펴보았습니다. FastAPI를 사용하여 SMTP를 통해 안전하고 신뢰할 수 있는 방법으로 이메일을 보낼 수 있습니다.