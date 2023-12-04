---
layout: post
title: "[python] python-dotenv를 사용하여 Azure Functions 설정 관리하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Azure Functions는 서버리스 컴퓨팅 플랫폼으로, 애플리케이션을 실행하기 위해 설정값들을 필요로 합니다. 이 설정값들은 Azure Portal에서 직접 관리할 수도 있고, 코드 내에서 하드코딩할 수도 있습니다. 하지만 코드에 설정값을 하드코딩하는 것은 보안상 좋지 않고, 유연성도 떨어지게 됩니다.

이런 문제를 해결하기 위해 `python-dotenv` 패키지를 사용하여 Azure Functions 설정값들을 관리하는 방법에 대해 알아보겠습니다.

## python-dotenv란?

`python-dotenv`는 dotenv 파일 형식으로 작성된 설정값들을 로드하여 환경 변수로 사용할 수 있게 해주는 패키지입니다. dotenv 파일은 설정값들을 키-값 형식으로 저장하는 파일로, 쉽게 작성하고 관리할 수 있습니다. 

## Azure Functions에 python-dotenv 적용하기

1. 먼저, `python-dotenv` 패키지를 설치합니다.

```python
pip install python-dotenv
```

2. Azure Functions 프로젝트의 루트 디렉토리에 `.env` 파일을 생성합니다. 이 파일에 설정값들이 저장될 것입니다.

3. `.env` 파일에 설정값들을 작성합니다. 예를 들어, 다음과 같이 작성할 수 있습니다.

```
MY_SETTING=Hello World
SECRET_KEY=abcd1234
```

4. Azure Functions 코드에서 `python-dotenv`를 사용하여 설정값들을 로드합니다.

```python
import os
from dotenv import load_dotenv

def get_setting(setting_name):
    return os.getenv(setting_name)

load_dotenv()

my_setting = get_setting("MY_SETTING")
secret_key = get_setting("SECRET_KEY")

print(my_setting) # 출력: Hello World
print(secret_key) # 출력: abcd1234
```

이제 `.env` 파일에 작성한 설정값들을 `load_dotenv()`를 호출하여 불러올 수 있게 되었습니다.

## dotenv 파일 관리하기

dotenv 파일은 `.env`라는 이름으로 저장되며, 파일명을 변경할 경우 `load_dotenv()`에서 파일명을 명시해주어야 합니다. 또한, dotenv 파일은 보안상 주의해야 하므로 gitignore 파일에 `.env`를 추가하여 코드 저장소에 업로드되지 않도록 해야 합니다.

## 결론

`python-dotenv`를 사용하면 Azure Functions 설정값들을 편리하게 관리할 수 있습니다. dotenv 파일을 사용하여 설정값을 하드코딩하지 않고 따로 관리함으로써 유연성과 보안성을 향상시킬 수 있습니다.