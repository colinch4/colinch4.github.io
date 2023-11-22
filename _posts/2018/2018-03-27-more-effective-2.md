---
layout: post
title: "항목 2 : 가능한 c++ 스타일의 캐스트를 즐겨 쓰자"
description: "캐스트(cast, 형변환)은 프로그래밍계의 1급 기피대상이다."
date: 2018-03-27
tags: [c++]
comments: true
share: true
---

캐스트(cast, 형변환)는 프로그래밍계의 1급 기피대상이다. 그럼에도 불구하고 프로그램을 작성하면서 사태가 걷잡을 수 없이 악화되면 어쩔 수 없이 이런 것들이 필요해 진다. 하지만, 어쨌든 어떤 타입을 아무 생각 없이 바꾸어 주는 C 스타일의 캐스는 있어야 할 것이 못된다. 그리고 눈에도 들어오지 않아 찾기도 힘들다. 때문에 이러한 방식의 캐스팅을 조금이라도 세심하게 조정해 주는 C++ 스타일의 캐스트를 쓰도록 하자.  
C++은 C 스타일 캐스트의 문제를 보완하기 위해 4가지 스타일의 캐스트 연산자를 도입했다. 보통 다음과 같이 쓴다.  
static_cast<타입>(표현식) 
```c++
int a, b; 
// double c = ((double)a)/b; // c 방식 
double c = static_cast<double>(a)/b; 
```
## static_cast 
static_cast는 **C 스타일 캐스트와 똑같은 의미와 형변환 능력을 가진 기본적인 캐스트 연산자**이다. C 스타일과 똑같다 보니 제약도 똑같은데, 예를 들어 struct를 int 타입으로 바꾸거나 double을 포인터로 바꾸는 일 같은 것은 할 수 없다. 또한 상수성(constness)을 떼어버리지도 못한다. 이런 일을 하는 캐스트 연산자인 const_cast를 보면 짐작은 할 수 있다.  
static_cast 외에 나머지 3개의 연산자는 좀더 구체적인 목적을 위해 만들어 졌다. 

## const_cast 
**const_cast는 상수성(constness)이나 휘발성(volatileness)를 없애는 데에 사용한다.** 이러한 캐스트가 쓰여진 소를 만나면 "아, 이 개발자는 const나 volatile로 선언한 표현에서 특성만 바꾸고 싶구나"라고 생각하면 된다. 이러한 의도는 컴파일러에 의해 더욱 확실해 지는데, 아래의 예제를 살펴보자. 
```c++
class A{...}; 
class B : public A {...}; 
void update(B *pb) {...}; 
B b; // b는 비상수 객체
const B& rb = b; // rb로 b를 상수 객체인것 처럼 참조 
// update(&rb); // error, const B*는 B*를 받는 함수에 넘길 수 없다. 
update(const_cast<B*>(&rb)); // 상수성이 제거 되어 이상 무
A *a = new B; 
// update(a); // error, a 타입은 A* 이지만, 함수는 B*를 받는다.
// update(const_cast<B*>(a)); // error, const_cast는 상수성이나 휘발성에만 영향을 줄때 유효 
```

## dynamic_cast
**dynamic_cast는 상속 계층 관계를 가로지르거나 하향시킨 클래스 타입으로 안전하게 캐스팅 할 때 사용한다.** 기본 클래스 객체에 대한 포인터나 참조자의 타입을 파생 클래스 타입으로 변환해 준다. 캐스팅 실패는 널 포인터(nullptr)나 예외를 보고 판별한다.  
```c++
class A{...}; 
class B : public A {...}; 
void update(B *pb) {...}; 
A *pa; 
...
update(dynamic_cast<B*>(pa)); // 이상무, pa를 B에 대한 포인터로 넘긴다.
void updateViaRef(B& rb) {...}; 
updateViaRef(dynamic_cast<B&>(*pa)); // 이상무, pa가 그 객체를 참조하고 있으면
```
dynamic_cast에도 제약이 있는데, 오로지 상속 계층 구조를 오갈 때만 사용하며, 게다가 가상 함수가 없는 타입에는 적용 할 수 없다. ( 자세한 내용은 [항목24](../../2018-03-27/more-effective-24/)를 참조) 물론, 상수성 제거에도 쓸 수 없다. 
```c++
int a, b; 
// double c = dynamic_cast<double>(a) / b; // error, 가상 함수가 전혀 없다. 
```

## reinterpret_cast
이 연산자가 적용된 후의 변환 결과는 거의 항상 컴파일러에 따라 다르게 정의되어 있다. 따라서 이 연산자가 쓰인 소스는 직접 이식이 불가능 하다.  
reinterpret_cast의 가장 흔한 용도는 함수 포인터 타입을 서로 바꾸는 것이다. 예를 들어 특정한 타입의 함수 포인터를 배열로 만들어 놓았다고 하고, 피치 못할 사정이 생겨 다른 타입의 함수의 포인터를 배열에 넣어야 할 경우가 생겼을 때 쓸 수 있다. 
```c++
typedef void (*FuncPtr)(); // 인자를 받지 않고, void를 반환하는 함수 포인터
FuncPtr fArr[10]; // FuncPtr 배열 
int doSomething(); 
// fArr[0] = & doSomething; // error, 타입 불일치 
fArr[0] = reinterpret_cast<FuncPtr>(&doSomething); 
```
하지만 이러한 캐스팅은 이식성을 떨어뜨리고, 어떠한 경우에는 캐스팅이 잘못된 결과를 낳기도 한다. ( [항목31](../../2018-03-27/more-effective-31/) 참조 ) 때문에 어떻게든 함수 포인터의 캐스팅은 피하자.  
  
> C++ 스타일의 캐스트 연산자는 보기도 썩 좋은 편도 아니고 키보드로 치기도 힘들다. 그러나 컴파일러와 다른 프로그래머에게 확실한 의미와 인식성을 선사한다는 점만 보아도 그리 튀는 단점은 아니라고 생각되지 않는다. 오히려 타입 캐스팅을 되도록 피해야 한다는 권장 사항에 부합?할수 있기 때문에 잘 한 일일지 모른다.  

