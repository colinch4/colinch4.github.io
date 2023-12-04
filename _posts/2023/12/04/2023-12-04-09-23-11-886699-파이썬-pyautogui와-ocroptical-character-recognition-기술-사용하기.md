---
layout: post
title: "[python] 파이썬 pyautogui와 OCR(optical character recognition) 기술 사용하기"
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

이번 포스팅에서는 파이썬의 pyautogui 라이브러리와 OCR 기술을 함께 사용하여 컴퓨터 화면에서 텍스트를 인식하는 방법에 대해 알아보겠습니다.

## pyautogui란?

pyautogui는 파이썬으로 작성된 자동화 라이브러리로, 컴퓨터 화면의 마우스 및 키보드 동작을 자동화할 수 있습니다. 이 라이브러리를 사용하면 특정 위치를 클릭하거나 키를 누르는 등의 작업을 파이썬 코드로 자동화할 수 있습니다.

pyautogui의 설치는 다음과 같이 pip 명령어를 통해 진행할 수 있습니다.

```python
pip install pyautogui
```

## OCR(optical character recognition)란?

OCR은 광학 문자 인식의 약자로, 이미지나 스캔한 문서에서 텍스트를 자동으로 인식하여 읽을 수 있도록 하는 기술입니다. OCR을 사용하면 컴퓨터 화면이나 이미지 등에서 텍스트를 추출하고 이를 다양한 용도로 활용할 수 있습니다.

OCR을 사용하는 라이브러리 중에는 Tesseract라는 라이브러리가 있습니다. 이 라이브러리는 구글에서 개발한 오픈 소스 OCR 엔진으로, 다양한 언어를 지원하고 높은 인식률을 자랑합니다.

Tesseract의 설치는 다음과 같은 명령어로 진행할 수 있습니다.

```python
pip install pytesseract
```

## pyautogui와 OCR을 함께 사용해보기

pyautogui와 OCR을 함께 사용하면 컴퓨터 화면에서 특정 위치의 텍스트를 추출할 수 있습니다. 아래는 이를 위한 간단한 예제 코드입니다.

```python
import pyautogui
import pytesseract
from PIL import ImageGrab

# 스크린샷을 가져옴
image = ImageGrab.grab()

# 이미지를 텍스트로 변환
text = pytesseract.image_to_string(image)

# 추출된 텍스트 출력
print(text)
```

위 코드에서는 pyautogui의 `ImageGrab.grab()` 함수를 사용하여 현재 화면의 스크린샷을 가져옵니다. 그리고 pytesseract의 `image_to_string()` 함수를 사용하여 해당 이미지에서 텍스트를 추출한 후, 추출된 텍스트를 출력합니다.

이 예제 코드를 실행하면 현재 화면에서 텍스트를 추출하는 결과를 확인할 수 있습니다.

## 마무리

이번 포스팅에서는 파이썬의 pyautogui와 OCR 기술을 함께 사용하여 컴퓨터 화면의 텍스트를 인식하는 방법에 대해 알아보았습니다. 이러한 기술을 응용하면 웹 스크래핑, 자동 문서 처리 등 다양한 자동화 작업에 활용할 수 있습니다.

더 자세한 내용을 알고 싶다면 pyautogui와 pytesseract의 공식 문서를 참조해보세요. 

- [pyautogui 공식 문서](https://pyautogui.readthedocs.io/en/latest/index.html)
- [pytesseract 공식 문서](https://github.com/madmaze/pytesseract)