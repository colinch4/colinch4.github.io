---
layout: post
title: "FastAPI와 Firebase Realtime Database를 연동하여 실시간 데이터 동기화하기"
description: " "
date: 2023-09-25
tags: [FastAPI, Firebase]
comments: true
share: true
---

FastAPI는 Python을 위한 빠르고 현대적인 웹 프레임워크이며, Firebase Realtime Database는 실시간으로 데이터를 동기화하는 NoSQL 데이터베이스입니다. 이 블로그 포스트에서는 FastAPI와 Firebase Realtime Database의 연동을 통해 실시간 데이터 동기화를 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. [Firebase 콘솔](https://console.firebase.google.com)에 접속하고, 새로운 프로젝트를 생성합니다.
2. 생성한 프로젝트에서 "Realtime Database"를 선택합니다.
3. "시작하기" 버튼을 클릭하여 데이터베이스를 만듭니다.
4. 데이터베이스의 규칙 설정에서, `".read"`와 `".write"` 규칙을 모두 `true`로 변경합니다. (테스트용으로만 사용하기 때문에 보안에 대한 고려는 나중에 합니다)

## FastAPI 프로젝트 설정

1. FastAPI 프로젝트를 생성합니다. 필요한 패키지를 설치하기 위해 다음 명령어를 실행합니다:

```python
pip install fastapi firebase-admin
```

2. Firebase Admin SDK를 초기화하기 위해 Firebase 프로젝트에서 제공되는 JSON 키 파일을 다운로드합니다.

3. FastAPI 프로젝트의 루트 경로에 다운로드한 키 파일을 저장합니다.

4. 다음과 같이 FastAPI 서버에서 Firebase Realtime Database를 초기화합니다:

```python
from fastapi import FastAPI
from firebase_admin import initialize_app
from firebase_admin import db

app = FastAPI()

# Firebase 초기화
initialize_app(options={
    'databaseURL': 'https://your-firebase-project-id.firebaseio.com',
    'credential': db.reference('/path/to/serviceAccountKey.json').get()
})

# FastAPI 라우터 정의
```

5. 이제 FastAPI에서 필요한 엔드포인트를 만들어서 Firebase Realtime Database와의 상호 작용을 구현할 수 있습니다. 예를 들어 새로운 데이터를 생성하는 엔드포인트를 다음과 같이 작성할 수 있습니다:

```python
@app.post('/data')
async def create_data(data: dict):
    # Firebase Realtime Database에 데이터 추가
    ref = db.reference('/data')
    new_data_ref = ref.push(data)
    return {"message": "Data created successfully"}
```

## 데이터 동기화

이제 FastAPI와 Firebase Realtime Database가 성공적으로 연동되었으므로, 데이터의 실시간 동기화를 구현할 수 있습니다. Firebase Realtime Database는 클라이언트 간의 데이터 변경 사항을 실시간으로 감지하고 업데이트하는 능력을 가지고 있습니다.

```python
# 데이터 변경 감지 콜백
def handle_data_change(event):
    print("Data changed:", event.data)
    # 여기서 FastAPI에서 수행할 작업을 구현합니다.

# 데이터 변경 감지 리스너 등록
ref = db.reference('/data')
ref.listen(handle_data_change)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

위와 같이 데이터 변경을 감지하는 콜백 함수를 등록하고, 해당 리스너를 통해 데이터의 변경 사항을 실시간으로 처리할 수 있습니다.

이제 FastAPI와 Firebase Realtime Database를 연동하여 실시간 데이터 동기화를 구현할 수 있습니다. 데이터의 생성, 수정, 삭제 등의 작업을 처리하는 FastAPI 엔드포인트를 정의하고, Firebase Realtime Database의 데이터 변경 감지를 통해 실시간으로 업데이트할 수 있습니다.

#FastAPI #Firebase