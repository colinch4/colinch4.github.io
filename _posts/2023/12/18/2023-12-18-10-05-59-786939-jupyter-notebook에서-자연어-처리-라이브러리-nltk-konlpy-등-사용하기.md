---
layout: post
title: "[python] Jupyter Notebook에서 자연어 처리 라이브러리 (nltk, konlpy 등) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

Jupyter Notebook은 데이터 분석과 시각화 작업을 위한 훌륭한 도구입니다. 이 튜토리얼에서는 Jupyter Notebook에서 자연어 처리를 위해 `nltk`(Natural Language Toolkit)와 `konlpy`(한국어 자연어 처리를 위한 패키지) 같은 라이브러리를 어떻게 사용하는지 알아보겠습니다.

## 목차
1. [nltk 라이브러리 사용하기](#nltk)
2. [konlpy 라이브러리 사용하기](#konlpy)

## nltk 라이브러리 사용하기
`nltk`는 Python에서 자연어 처리를 수행하기 위한 풍부한 기능을 제공하는 라이브러리입니다. Jupyter Notebook에서 `nltk`를 사용하려면 먼저 라이브러리를 설치해야 합니다. 다음은 `nltk`를 설치하는 방법입니다.

```python
!pip install nltk
```

설치가 완료되면 다음과 같이 `nltk`를 활용하여 텍스트 데이터를 토큰화하거나 형태소 분석을 수행할 수 있습니다.

```python
import nltk
nltk.download('punkt')

text = "Natural Language Processing is a complex field but also interesting."
tokens = nltk.word_tokenize(text)
print(tokens)
```

## konlpy 라이브러리 사용하기
한국어 자연어 처리를 위한 `konlpy` 라이브러리도 Jupyter Notebook에서 사용할 수 있습니다. 먼저 `konlpy`를 설치합니다.

```python
!pip install konlpy
```

설치가 완료되면 다음과 같이 `konlpy`를 통해 한글 문장을 형태소로 분석할 수 있습니다.

```python
from konlpy.tag import Okt

okt = Okt()
text = "자연어 처리는 인공지능의 중요한 부분입니다."
morphs = okt.morphs(text)
print(morphs)
```

이제 Jupyter Notebook에서 `nltk`와 `konlpy` 라이브러리를 사용하는 방법을 알았습니다.

## 결론
Jupyter Notebook을 통해 `nltk`와 `konlpy`와 같은 자연어 처리 라이브러리를 사용할 수 있어서 텍스트 데이터에 대한 다양한 분석을 쉽게 수행할 수 있습니다.

## 참고 문헌
- nltk 공식 웹사이트: https://www.nltk.org/
- konlpy 공식 웹사이트: https://konlpy.org/en/latest/
- Jupyter Notebook 공식 웹사이트: https://jupyter.org/