---
layout: post
title: "FastAPI와 OCR(Optical Character Recognition)을 활용하여 문자 인식 서비스 구현하기"
description: " "
date: 2023-09-25
tags: [FastAPI)]
comments: true
share: true
---

![OCR](https://example.com/ocr.jpg)

문자 인식은 현대 디지털 시대에서 매우 중요한 기술입니다. OCR (Optical Character Recognition)은 이미지 상의 문자를 인식하여 텍스트로 변환하는 기술을 말합니다. 이번 포스트에서는 FastAPI와 OCR을 결합하여 문자 인식 서비스를 구현하는 방법에 대해 알아보겠습니다.

## FastAPI 소개
FastAPI는 Python으로 작성된 빠르고 (참고: #FastAPI), 현대적인 웹 프레임워크로, 비동기적이고 효율적인 API를 쉽게 개발할 수 있게 해줍니다. FastAPI의 장점은 다음과 같습니다.

- 빠른 실행 속도와 뛰어난 성능
- 자동 생성된 문서와 상호작용 가능한 API 문서
- 데이터 유효성 검사 및 자동 문서화를 지원하는 Pydantic 모델 사용
- 기본적인 인증과 보안 기능
- ASGI 서버 지원 (Uvicorn, Hypercorn 등)

## OCR 모듈 선택
OCR을 구현하기 위해 다양한 라이브러리와 모듈 중에서 선택해야 합니다. 여기에서는 Tesseract OCR을 사용하여 문자 인식을 수행합니다. Tesseract OCR은 Google에서 개발한 오픈 소스 OCR 엔진으로, 높은 정확도와 다양한 언어 지원으로 유명합니다.

## FastAPI와 OCR 통합하기
아래는 FastAPI를 사용하여 OCR 서비스를 구현하는 예시 코드입니다.

```python
from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image

app = FastAPI()

@app.post('/ocr')
async def ocr(file: UploadFile = File(...)):
    image = Image.open(file.file)
    text = pytesseract.image_to_string(image)
    return {'text': text}
```

위 예제에서는 `/ocr` 엔드포인트를 만들었습니다. 클라이언트는 `multipart/form-data`로 이미지를 업로드하고, 서버는 해당 이미지를 OCR을 수행하여 인식된 텍스트를 반환합니다. `pytesseract` 모듈의 `image_to_string` 함수를 사용하여 이미지에서 텍스트를 추출하고, 추출된 텍스트를 응답으로 반환합니다.

## 실행 및 테스트
이제 FastAPI 애플리케이션을 실행하고 테스트하는 방법을 알아보겠습니다. 먼저, 필요한 패키지를 설치해야 합니다.

```bash
pip install fastapi uvicorn pytesseract pillow
```

다음으로, 애플리케이션을 실행합니다.

```bash
uvicorn main:app --reload
```

마지막으로, Postman 또는 CURL을 사용하여 OCR 서비스를 테스트할 수 있습니다.

```bash
curl -X POST -F 'file=@image.jpg' http://localhost:8000/ocr
```

위 명령어에서 `image.jpg`는 테스트할 이미지 파일명입니다.

이제 FastAPI와 OCR을 통해 문자 인식 서비스를 구현하는 방법을 알게 되었습니다. OCR은 다양한 분야에서 활용할 수 있는 강력한 기술이므로, 상황에 맞게 응용해보시기 바랍니다. #OCR

참고 링크:
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)