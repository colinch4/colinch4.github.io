---
layout: post
title: "[java] 불변 객체(Immutable Object)"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---


# 불변 객체(Immutable Object)

> 불변 객체란?

- 생성 이후에 객체 상태를 변경할 수 없는 객체.

> 불변 객체의 장점

- 동일한 내용의 객체를 공유할 수 있다.
- Flyweight Pattern
- 동일한 내용의 경우 공유할 수 있으므로, 객체를 비교할 때, == 연산을 통해 비교할 수 있다. (==: 참조 동일성 판단, equals: 객체 동등성 판단)
- 객체 상태가 변경되지 않으므로 멀티 스레드에서 사용 시 동기화가 필요없다. 


```
> String vs StringBuilder

    class Program{
    @Test
    void foo1(){
        String s ="";
        for(int i=0; i<1000000; i++){
            s+=i;
        }
    }
    @Test
    void foo2(){
        StringBuilder s = new StringBuilder("");
        for(int i=0; i<1000000; i++){
            s.append(i);
        }
    		s.toString();
    }
    
    }
```

- String 클래스는 for문을 돌릴 때마다 새로운 객체를 생성하기 때문에 시간이 매우 오래 걸리지만, StringBuilder 클래스는 for문을 돌릴 때마다 원래의 객체에 값을 추가하므로 시간이 매우 적게 걸린다.

- String은 immutable하고 StringBuilder은 mutable하다. 그렇기 때문에 위 처럼 for문을 돌릴 때마다 새로운 객체를 생성하는 이유는 String이 불변 클래스이기 때문에 값을 바꿀 때 마다 새로운 객체를 생성해낸다. 
하지만 StringBuilder는 mutable하기 때문에 값을 바꾼다고 하여도 바꾸는 것에 따라서 공간이 유동적으로 바뀌기 때문에 새로운 객체들을 만들어내지 않는다.

### COW(Copy On Write) ⇒ lazy copy

- 객체를 바로 복제하지 않고 동일한 객체를 참조하다가, 수정이 필요할 경우 객체를 복제해서 새로운 참조를 만드는 기법 @형규 함
