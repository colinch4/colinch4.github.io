---
layout: post
title: "[python] Requests 라이브러리를 이용해 Delayed Response 요청을 보내는 방법은?"
description: " "
date: 2023-11-22
tags: [python]
comments: true
share: true
---

Python의 Requests 라이브러리는 HTTP 요청을 보내고 응답을 받는 데 사용되는 인기 있는 라이브러리입니다. Delayed Response 요청은 서버로 요청을 보내고 일정 시간동안 응답을 기다린 후에 응답을 받는 기능을 말합니다. 이러한 요청을 보내기 위해서는 Requests의 timeout 파라미터를 사용할 수 있습니다.

아래는 Requests를 사용하여 Delayed Response 요청을 보내는 예제입니다.

```python
import requests

# 요청을 보낼 URL
url = "https://www.example.com/"

# timeout 설정을 통해 응답을 기다리는 시간을 조절할 수 있습니다. 여기서는 5초로 설정합니다.
response = requests.get(url, timeout=5)

# 응답 코드 확인
if response.status_code == 200:
    print("요청이 성공적으로 완료되었습니다.")
    print("응답 내용:", response.text)
else:
    print("요청이 실패하였습니다. 응답 코드:", response.status_code)
```

위의 예제에서는 `requests.get()` 함수를 사용하여 GET 요청을 보냅니다. `timeout` 파라미터를 5로 설정하여 5초 동안 응답을 기다립니다. 만약 응답이 5초 이내에 받아지지 않으면 TimeoutError가 발생합니다. 응답을 받은 후에는 응답 코드를 확인하고 성공 여부에 따라 처리할 수 있습니다.

참고로, Timeout 값을 조정하여 원하는 시간만큼 응답을 기다릴 수 있습니다. 작은 값으로 설정하면 응답을 빨리 받을 수 있지만, 너무 작게 설정할 경우 응답을 받지 못할 수도 있으니 적절한 값을 설정해야 합니다.

참조: 
- Requests 라이브러리 문서: https://requests.readthedocs.io/
- Python 공식 문서: https://docs.python.org/3/library/urllib.request.html