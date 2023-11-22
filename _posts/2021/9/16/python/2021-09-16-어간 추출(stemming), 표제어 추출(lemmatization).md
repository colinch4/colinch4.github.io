---
layout: post
title: "[파이썬] 어간 추출(stemming), 표제어 추출(lemmatization)"
description: " "
date: 2021-09-16
tags: [python]
comments: true
share: true
---


## 어간 추출(stemming), 표제어 추출(lemmatization)

위 두개는 서로 다른 언어들이지만 하나로 일반화 할 수 있으면 일반화하자는 의의, 

단어 개수를 최대한 줄여보자에 의미가 있다.

## 1. 표제어 추출(lemmatization)

표제어 추출은 서로 다른 단어임에도 뿌리를 찾아 단어를 줄일 수 있는지 판단합니다.

ex) am, are, is -> be

표제어 추출을 하는 가장 섬세한 방법은 형태학적 파싱을 하는 것

형태학이랑 형태소로 부터 단어를 만들어가는 학문

형태소란 의미를 가진 가장 작은 단위 라는 뜻

형태소는 두 가지 종류가 있다.

- 어간 (stem) : 단어에 의미를 담고있는 단어의 핵심 부분
- 접사 (affix) : 단어에 추가적인 의미를 주는 부분

ex) cats -> cat(어간), -s(접사)

```python
import nltk
from nltk.stem import WordNetLemmatizer ## 표제어 추출 도구
```

## 2. 어간 추출(stemming)

어간 추출은 형태학적 분석을 단순화한 버전이라 보면 된다. 정해진 규칙만을 보고 단어의 어미를 자르는 어림짐작의 작업

ex) alize -> al , ance -> 제거 , ical -> ic 등 규칙을 갖는다

ex) formalize -> formal,  allowance -> allow , electricical -> electric

ex) this -> thi , was -> wa 등 규칙에 의해 작동되기 때문에 사전에 없는 단어들이 포함될 수 있다.

```python
import nltk
from nltk.stem import PorterStemmer
s = PorterStemmer()
words=['formalize', 'allowance', 'electricical']
[s.stem(w) for w in words]

## w => ['formal', 'allow', 'electric']
```

porter 알고리즘을 사용할 때는 porter 알고리즘의 상세규칙을 살펴 볼 필요가 있다.

```python
import nltk
from nltk.stem import LancasterStemmer
```

위에 코드는 porter 와 다른 알고리즘 , 규칙이 조금씩 다르므로 규칙들을 살펴 봐야된다.



## 3. 한국어

한국어는 너무 불규칙적이라 사용하기 어려워 보인다. 예를 들어 ''잡다'' 를 보면 "잡","다"를 

"잡"(어간),"다"(어미)로 구분 된다.

- 어간(stem) : 용언(동사,형용사)를 사용할 때, 원칙적으로 모양이 변하지 않는 부분, 때로는 어간도 바뀔 수 있음(예: 긋다, 긋고, 그어서, 그어라)
- 어미(ending) : 용언의 어간 뒤에 붙어 활용하며 변하는 부분, 여러 문법적 기능 수행, 규칙이 있으면 규칙 활용, 불규칙이면 불규칙 활용

