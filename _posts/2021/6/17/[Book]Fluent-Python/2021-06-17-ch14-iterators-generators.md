---
layout: post
title: "[Fluent Python] 14장 반복형, 반복자, 제너레이터"
description: " "
date: 2021-06-17
tags: [book]
comments: true
share: true
---

## 반복형, 반복자, 제너레이터

> 데이터를 처리할 때 반복은 기본이다.

메모리에 다 들어가지 않는 데이터를 반복하기 위해서는 항목들을 느긋하게 가져와야 한다.

파이썬은 리스프와 달리 매크로가 없고, 반복자 패턴을 추상화할 수 있게 yield 키워드를 제공한다. 2011년 2.2버전에 추가되었으며, 제너레이터를 생성한다.

모든 제너레이터는 반복자이다. 제너레이터는 무한 수열을 표현할 수 있으나, 컬렉션에는 저장할 수는 없다. 이러한 차이에도 불구하고, 일반적으로 반복자와 제너레이터를 거의 동일시 한다.

## 단어 시퀀스

Sentence 클래스를 만들어서, 문장을 입력하면, 내부적으로 단어별로 저장하고, 이용함으로써 반복형에 대해서 살펴본다.

시퀀스는 반복할 수 있는데, 그 이유는 ```iter()```함수 때문이다.
1. 객체가 ```__iter__()``` 메서드를 구현하는지 확인하고, 구현되어 있으면 호출하여 반복자를 가져온다.
1. 구현되어 있지 않다면, ```__getitem__()```이 구현되었는 확인하며, 구현되어 있다면 인덱스가 0에서 시작하는 차례래로 반복하는 반복자를 생성한다.
1. 이 과정 모두가 실패하면 `TypeError`를 발생시킨다.

반복가능함을 확인하기 위해서는 `abc.Iterable`의 하부 클래스인지 확인해보면 되지만, 이 경우에는 ```__iter__()``` 메서드의 유무만 검사하므로, 저자는 `iter(x)`를 호출하고, `TypeError`를 처리하는 방식으로 확인하는 방법을 제안하고 있다.

**반복형**은 `iter()` 내장함수가 호출될 수 있는 모든 객체와 **반복자**를 반환하는 ```__iter__()``` 메서드를 구현한 객체이다.
**반복자**는 자료형이 아니라 프로토콜이며, 다음 항목을 반환하거나 항목이 없을 때 StopIteration 예외를 발생시키는 인수를 받지 않는 ```__next__()```메서드를 구현할 객체를 의미한다.
파이썬의 반복자는 ```__iter__```와 ```__next__``` 속성으로 갖고 있으며, 따라서 반복형이기도 하다.

## 고전적인 반복자

디자인 패턴에서 설명하는 반복자 디자인 패턴이다. 

앞서 만든 `Sentence` 클래스에서 반복형인 `SentenceIterator`를 돌려준다. 매우 간단하게 구현할 수 있는데, 잘못된 방법에 대해서 살펴보자.

`Sentence` 자체를 반복자로 만드는 것인데, 이는 반복형과 반복자를 구분하지 못하기 때문에 발생하는 문제이다.

반복자는 반복형이지만, 반복형은 반복자가 아니다.

디자인 패턴에서는 반복자 패턴은 다음과 같은 용도에 사용하도록 설명하고 있다.

* 집합 객체의 내부 표현을 노출시키지 않고 내용에 접근하는 경우
* 집합 객체의 다중 반복을 지원하는 경우
* 다양한 집합 구조체를 반복하기 위한 통일된 인터페이스를 제공하는 경우

즉, 다중 반복을 지원하기 위해서는 여러개의 독립적인 반복자를 가질 수 있어야 하며, 각 반복자는 고유한 내부 상태를 유지해야 한다.

## 제너레이터

본체 안에 yield 키워드를 가진 함수는 모두 제너레이터 함수이다.

앞선 예제에서 ```__iter__()``` 함수에 제너레이터를 이용해서 구현하면, yield 문에서 제너레이터 객체가 생성된다. 그러므로 더 이상 SentenceIterator가 필요치는 않다.

제너레이터는 값을 생성한다고 표기하였는데, 이는 함수와 구별하기 위함이다. 함수는 값을 '반환'하지만, 제너레이터 함수는 제너레이터 객체를 '반환'한다. 그리고 제너레이터 객체가 값을 생성한다. 제너레이터 함수에서 `return`은 `StopIteration` 예외를 발생하게 만든다.

## 느긋한 구현

느긋한 계산법의 반대는 조급한 계산법(eager evaluation).

`re.findall()` 대신 `re.finditer()`를 이용하여 호출할 때 단어를 나누기 시작한다.

## 제너레이터 표현식

지능형 리스트 표현식과 유사하게 튜플처럼 생성하면, 튜플이 아니라 제너레이터가 생성된다.

핵심코드는 다음과 같다.

```python
RE_WORD = re.comile('\w+')
class Sentence:
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
```

## 제너레이터 표현식은 언제 사용하는가?

제너레이터 표현식은 함수를 정의하고 호출할 필요없이 제너레이터를 생성할 수 있는 편리 구문(sugar syntax)이다. 반면 제너레이터 함수는 융통성이 훨씬 큰데, 복잡한 논리를 구성할 수 있고, 코루틴으로 사용할 수도 있다.

일반적으로 제너레이터 표현식을 이용하면 되고, 한줄로 표현할 수 없을 때는 가독성을 위해서 제너레이터 함수를 이용한다. 제너레이터 함수를 이용ㅉ하면 이름을 가지고 있기 때문에 재사용을 할 수 있다는 이점도 있다.

제너레이터 표현식을 함수의 인자로 넘겨줄 경우, 제너레이터 표현식이 유일한 인자라면, 괄호는 2개쓰지않고, 1개만 쓴다.

## 등차수열 제너레이터

`range()`는 정수로 구성된 유한 등차수열을 생성하며, `itertools.count()`는 무한 등차수열을 생성한다.

`itertools.count()`는 인수를 지정하지 않으면, 0부터 시작하는 수열을 생성하고, 두 개의 인자를 주면, start와 step이 된다.

`itertools.takewhile()`은 제너레이터를 소비하면서 주어진 조건식을 만족할 동안 반복하는 제너레이터를 생성한다.

## 표준 라이브러리의 제너레이터 함수

`os.walk()`는 제너레이터 함수이다.

`itertools.compress(it, selector_it)` 함수는 R에서 레코드를 걸러 내는 것처럼, 뒤의 인자를 순회하면서 참일 경우만, 앞의 인자값을 뽑아낸다. `vlookup`과도 유사

`itertools.accumulate(it,  [func])`은 값을 누적한다. 함수를 인자로 넘겨주면 해당함수를 누적하여 적용한다. 최저값만 남긴다던지, 최대값을 남긴다던지 할 수 있다.

`map`은 첫번째 인자의 함수를 2번째부터 주어진 인자를 넘겨서 계산한다.

`itertools.starmap`은 `map`과 유사하나 뒤에 주어진 반복자를 해체하여(*), 적용시킨다. 즉, 주어진 반복자가 한 번 반복때마다 여러개의 속성을 가질 때, (enumerate는 2개) 이걸 풀어서 n개의 인자를 준 것처럼 넘겨준다. 이동평균 예시는 다음과 같다.

```python
list(iterools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1)))
```

`itertools.chain(it1, ..., itN)`는 반복자를 차례대로 하나씩 풀어서 다 붙여준다.

`itertools.chain.from_iterable(it1, ..., itN)`는 차례대로 붙여주되, 주어진 반복자가 반복가능하면 그것 역시 풀어서 붙여준다.

`zip`는 주어진 반복자를 병렬로 붙여서 튜플을 만들어준다. 지퍼를 생각하면 쉽다.

`itertools.zip_longest(it1, ..., itN, fillvalue=None)`은 zip과 동일하나 가장 긴 반복자 길이만큼 반복하고, 모자라는 값을 `fillvalue`로 채운다.

`itertools.product()`는 주어진 반복자의 조합을 만드는데, `repeat` 인자를 이용하면, 주어진 항목의 총 조합을 만들수 있다.

`itertools.combinations(it, out_len)`은 순열 조합을 만든다.

`itertools.combinations_with_replacement(it, out_len)`은 뽑았던 공을 다시 넣고 뽑는 방식의 순열 조합을 만든다. 앞서 product와 유사하나 뽑힌 조합의 순서가 의미가 없다. 즉 순열조합에서는 ('A', 'B')와 ('B', 'A')는 동일하고, 한번만 등장한다.

`itertools.cycle(it)`은 각 항목의 사본을 저장 후, 무한히 반복한다.

순열조합 제너레이션 함수는 `itertools.combinations`, `itertools.combination_with_replacement`, `itertools.permutations`, `itertools.product`가 있다.

`itertools.groupby(it, key=None)`는 주어진 반복형을 그룹으로 나눈다. 나누어진 그룹 제너레이터는 `list()` 내장함수를 통해 시퀀스로 변환할 수 있다.

`itertools.tee(it, n=2)`는 반복형을 이용하여 여러개(n)의 제너레이터를 생성한다.

## yield from

```python
for i in it:
    yield i
```

위 코드는 아래와 동일하다.

```python
yield from it
```

## 반복형을 리듀스하는 함수

`all(it)`, `any(it)`, `max(it)`, `min(it)`, `functools.reduce(func, it, [init])`, `sum(it)` 등이 있다. `all([])`은 `True`를 리턴하며, `any([])`은 `False`를 리턴한다.

## iter() 함수 들여다보기

어떤 객체 `x`를 반복해야 할 때, `iter(x)`를 호출할 수 있으며, 두번째 인자를 주면, 콜러블 객체가 두번째 인자와 같은 값을 리턴하면 `StopIteration` 예외가 발생한다. 두번째 값으로 지정된 구분표시(sentinel)은 절대 리턴되지 않는다.

## 사례연구

필자가 레거시 데이터베이스를 변환하는 과정에서 2개 이상의 이종 데이터베이스를 처리하기 위해서 제너레이터를 이용하여 구현했다는 이야기. 제너레이터를 통해서 메모리를 많이 쓰지 않고, 읽고 쓰기를 번갈아 수행할 수 있었고, 로직에서 읽는 부분을 분리해냄으로써, 다양한 형태에 대하여 유연하게 대처할 수 있었다.

소스코드는 [fluentpython/isis2json](http://bit.ly/1HGqzzT)에 올려두었다고 한다.

## 코루틴으로서의 제너레이터

파이썬 2.2에서 yield가 추가되었는데, 5년 후 2.5버전에서 `PEP 342 - 향상된 제너레이터를 이용한 코루틴` 제안서에서 `send()` 등의 메서드를 추가하였다. `send()`는 `__next__()`와 유사하나 데이터를 보낼 수 있다.

데이비드 비즐리는 [PyCon US 2009](http://www.dabeaz.com/coroutines/Coroutines.pdf)에서 다음과 같이 경고하였다.

* 제너레이터는 반복을 위한 데이터를 생성
* 코루틴은 데이터 소비자
* 두 개념을 섞지 마라.
* 코루틴은 반복과 상관없다.
* 주의: 코루틴 안에서 yield가 값을 생성하게 하는 것은 쓸모 있지만, 반복과 상관없다.

코루틴은 [16장](ch16-coroutine.md)를 참조하자.

## 읽을거리

* 공식 레퍼런스의 [yield 표현식](http://bit.ly/1MM5Xb5)
* [itertools 모듈 문서](https://docs.python.org/3/library/itertools.html)는 모든 예제를 망라해 두었다.
* [itertools 비법](http://bit.ly/1MM5YvA)

제너레이터를 위한 특수한 키워드(`def` 같은)가 필요하다고 주장하는 경우가 있고, 저자도 동의하는 바이나, "자비로운 종신 독재자"는 새로운 키워드를 추가하지 않았다.
