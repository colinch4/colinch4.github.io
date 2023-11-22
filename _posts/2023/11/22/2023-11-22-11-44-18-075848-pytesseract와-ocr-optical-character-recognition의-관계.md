---
layout: post
title: "[python] PyTesseract와 OCR (Optical Character Recognition)의 관계"
description: " "
date: 2023-11-22
tags: [python]
comments: true
share: true
---

OCR (Optical Character Recognition)은 광학 문자 인식 기술로, 이미지나 스캔된 문서에서 텍스트를 인식하는 기술입니다. 이 기술은 다양한 분야에서 활용되며, 예를 들어 문서 스캐닝, 번역, 데이터 추출 등에 사용됩니다.

PyTesseract는 Python에서 OCR을 수행하기 위한 인기 있는 라이브러리입니다. 이 라이브러리는 Google의 Tesseract OCR 엔진을 Python에 쉽게 연결하여 사용할 수 있게 해줍니다. Tesseract는 C++로 작성된 오픈 소스 OCR 엔진으로, 다양한 언어를 지원하며 높은 인식률을 보여줍니다.

PyTesseract는 간단하고 사용하기 쉬운 API를 제공하여 이미지나 스캔된 문서로부터 텍스트를 추출할 수 있습니다. 아래는 PyTesseract를 사용하여 OCR을 수행하는 간단한 예시 코드입니다.

```python
import cv2
import pytesseract

# 이미지 불러오기
image = cv2.imread('example_image.jpg')

# 이미지 전처리
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OCR 수행
text = pytesseract.image_to_string(gray, lang='eng')

# 결과 출력
print(text)
```

위의 코드에서는 OpenCV를 사용하여 이미지를 불러오고, 이미지를 회색으로 변환한 후 PyTesseract를 사용하여 텍스트를 추출합니다. 결과로 추출된 텍스트를 출력합니다.

PyTesseract를 사용하기 위해서는 먼저 Tesseract OCR 엔진을 설치해야 합니다. 각 운영체제에 맞는 설치 방법은 PyTesseract의 공식 문서에서 확인할 수 있습니다.

PyTesseract는 많은 옵션을 지원하며, 세밀한 설정을 통해 인식률을 높일 수 있습니다. 또한 다국어 인식에도 좋은 성능을 보여주므로 다양한 언어로 된 문서에서도 효과적으로 사용할 수 있습니다.

참고 문헌:
- PyTesseract 공식 문서: [https://pypi.org/project/pytesseract/](https://pypi.org/project/pytesseract/)
- Tesseract OCR 공식 사이트: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)