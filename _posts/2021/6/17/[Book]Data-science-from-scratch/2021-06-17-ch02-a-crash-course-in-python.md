---
layout: post
title: "[파이썬 속성 강좌] 기본기"
description: " "
date: 2021-06-17
tags: [book]
comments: true
share: true
---

## 파이썬 속성 강좌

초심자가 처음보고 이해하기엔 무리가 있겠지만, 단시간(1시간이내)에 파이썬을 실용적인 수준까지 쓸 수 있도록 안내하고 있다.

## 기본기

### 설치하기

아나콘다 배포판을 이용하자.

### The zen of python

파이썬의 교리 같은 것인데, ```import this```를 하면 볼 수 있다. 기본적으로 단순하게, 그리고 작동하는 데 집중하길 권하고 있다. 헬로월드 예제를 자바랑 비교해보면 명확하다. 자바는 OOP를 위해서 필요한 형식을 다 갖추다보니, 헬로월드가 5줄은 된다. 거기다가 사용해야 하는 키워드도 굉장히 많다. 하지만 파이썬은 그저 ```print("hello, world")```가 전부이다.

### 들여쓰기

파이썬은 여느 언어와 달리 대괄호로 블록을 구분하지 않고, 들여쓰기로 블록을 구분한다. 그리고 들여쓰기 과정에서 탭과 스페이스를 혼용하면 안되는데, 초심자 입장에서는 이점이 어렵게 느껴질 수 있다. 반면 포맷이 일정부분 강제되기 때문에 가독성이 좋아진다는 장점이 있다. 줄바꿈을 하고 싶으면, 괄호를 열어서 나열하거나, 역슬래시를 써서 해당 줄의 입력이 끝나지 않았음을 인터프리터에게 알릴 수 있다. 또한 중간에 빈 줄이 들어갈 경우, 오작동할 수 있으므로 초심자는 조심하자.

### 모듈

라이브러리, 패키지, 외부함수 등등 초심자나 다른 언어를 이용하는 사람들이 다양하게 부르는 용어일텐데, 파이썬에서는 모듈이라고 한다. 모듈을 가져오는 방식은 몇가지가 있는데, 형태에 익숙하면 된다. 파이썬은 기본적으로 영어로 읽을 때 편하게 코드가 읽히도록 설계되었음을 염두해서 기억하면 도움이 된다.

```python
import re
import re as regex
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
```

### 연산

프로그래밍 언어는 자료형에 따라 연산이 다소 다를 수 있다. 대표적인 것이 나눗셈일텐데, `5/2`는 정수형이기 때문에 `2`가 된다. 실수형으로 계산하면 일반적으로 원하는 결과를 얻을 수 있고, 몫을 구하고 싶으면 `5//2`로 계산할 수 있다. 나머지는 `5%2`이다.

### 함수

파이썬의 함수는 일급 함수의 특징을 갖는데, 함수 자체도 변수로 넘겨줄 수 있다.

람다 함수는 다소 생소한데, 이름없는 함수 정도로 이해하고, 형식에 그저 익숙해지면 된다.

### 문자열

유니코드(한글)를 쓴다면, 무조건 python3를 쓰길 강력 권한다. 간혹 2.7 혹은 2.x 버전을 쓰는 경우가 있는데, 문자열 처리가 쉽지 않다. 파이썬 3에서 무조건 utf-8로 코드를 작성하면 별다른 문제가 없다.

### 예외 처리

여타 언어처럼 예외 처리가 있다. ```try```, ```expect``` 키워드를 이용한다.

### list

파이썬을 처음 쓸 때 매력적으로 느껴졌던 게 바로 리스트이다. C언어에서 힘들게 쓰던 배열을 아주 쉽게 list를 이용하여 구현된다. 가장 기본적인 자료형이며, 인덱스 사용법 정도는 익혀두자.

리스트에 항목이 존재하는 지 평가하기 위한 ```in``` 키워드, 리스트 2개를 합칠 때는 ```my_list.extend()``` 메서드, 항목을 하나씩 추가할 때는 ```my_list.append()``` 메서드를 이용하면 된다.

그리고 파이썬에서는 언팩이 지원되므로, 두 변수를 서로 바꾸는 swap 기능을 한줄로 표현할 수 있다.

### tuple

리스트와 유사하나 불변형 자료형이다.

### dict

사전형 자료형으로 자주 이용된다. 키가 없을 때는 에러가 발생하므로, 예외처리 혹은 defaultdict 같은 자료형을 이용하여 구현하도록 한다.

### defaultdict

사전형을 이용하는 케이스 중, 자료을 단순히 채워가는 경우가 있는데, 이 경우 키의 존재 여부를 매번 평가하도록 코드를 작성하는 것이 번거로울 수 있다. 이 때, defaultdict를 이용하면, 값이 없으면, default 값을 제공함으로써, 예외처리나 비교구문 없이 구현이 가능하다.

비슷한 기능을 수행하는 클래스로 ```Counter```가 있다.

### set

수학의 집합 개념인 ```set```은 순서가 상관없고, 중복을 허용하지 않고, 존재 여부가 중요할 때 이용할 수 있다.

### 흐름 제어

대부분의 언어와 유사한 흐름 제어 구문을 가지고 있으며, ```while```보다는 ```for```구문을 훨씬 많이 쓴다.

### True/False

파이썬은 참과 거짓을 나타내는 자료형의 값으로 ```True```와 ```False```를 쓴다. 기본 룰을 C와 유사한데, 코드를 작성할 때 암시적 룰에 기대하기 보다는 명시적으로 작성해주는 것이 좋다.

## 한걸음 나아가기

### 정렬

```sorted()``` 함수 혹은 ```list_a.sort()```와 같이 쓸 수 있다. 전자는 새로운 객체를 돌려주지만, 후자는 객체 내용을 바꾼다.

### List Comprehension

리스트 형태의 자료를 만드는 구문으로 굉장히 유용하다. 꼭 익혀두길 바란다. 다음과 같은 예제를 보면 좀 더 쉽게 이해가 될 것 같다.

```python
[x for x in range(5) if x % 2 == 0]
[x * x for x in range(5)]
```

### Generator와 iterator

제너레이터는 함수를 한꺼번에 실행해서 결과를 전부 주는 것이 아니라, 필요할 때 하나씩 돌려주는 방식을 구체화한 기능이다. ```yield``` 키워드를 이용하는데, 자세한 건 다른 교재를 좀 더 참조하자.

### 난수 생성

```rand()``` 함수를 이용할 수 있다. 시드를 지정하면, 동일한 난수를 생성할 수 있다.

### 정규표현식

문자열 처리에 정규표현식이 모든 해법을 제시해 준다. 반드시 쓸 필요는 없지만, 다소 복잡한 패턴을 문자열에서 찾아야 한다면, 정규표현식이 가장 근사한 해법이다.

### 객체 지향 프로그래밍

파이썬도 객체지향프로그래밍을 지원한다. ```class```가 있다는 말인데, 여타 언어와는 다소 다른 구문을 가지고 있으니, 시간을 두고 살펴보자.

### 함수형 도구

함수의 고정된 인자를 추출해서 줄여주는 ```partial```이라던지, ```map```, ```reduce```같은 함수를 도와주는 함수가 있다.

### enumerate

자바를 꽤 오래 사용했던 터라, 배열을 다룰 때 항상 인덱스를 이용하는데, 파이썬에서는 리스트의 반복형을 이용하므로 인덱스를 잘 쓰지 않는다. 인덱스가 필요할 때 ```enumerate```를 이용하면 인덱스를 구할 수 있다.

### zip과 unpacking

```zip```는 인자로 주어진 가장 짧은 리스트의 항목 수 길이만큼의 새로운 리스트를 만들어 주는데, 주어진 항목의 서로 매칭해서 리스트를 만든다. 양쪽 지퍼를 매칭해서 잠그는 것을 연상하면 쉽다.

### args와 kwargs

인자를 받을 때, ```*```로 받으면 튜플로, ```**```로 받으면 dict로 매개변수를 받아준다.
