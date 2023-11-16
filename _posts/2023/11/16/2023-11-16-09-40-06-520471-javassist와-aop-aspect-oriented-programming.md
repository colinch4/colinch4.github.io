---
layout: post
title: "[java] Javassist와 AOP (Aspect-Oriented Programming)"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Javassist와 AOP (Aspect-Oriented Programming)에 대해 알아보겠습니다.

## Javassist란?

Javassist는 Java 프로그래밍 언어를 위한 바이트 코드 조작 도구입니다. 이 도구를 사용하면 실행 중인 프로그램의 클래스 파일을 동적으로 수정하고 생성할 수 있습니다. Javassist는 자바 어플리케이션에서 리플렉션을 사용하지 않고도 클래스 파일을 변경할 수 있는 강력한 기능을 제공합니다.

Javassist는 많은 기능을 제공하지만, 여기서는 AOP와의 관련성에 초점을 맞출 것입니다.

## AOP (Aspect-Oriented Programming)란?

AOP (Aspect-Oriented Programming)는 프로그래밍 패러다임의 한 종류로, 관심사를 분리하고 모듈화하는 것을 목표로 합니다. 전통적인 프로그래밍 방식에서는 프로그램의 여러 부분에 흩어진 관심사를 한 곳에서 모두 처리해야 할 수도 있습니다. 하지만 AOP를 사용하면 이러한 관심사들을 개별적으로 분리하여 처리할 수 있습니다.

## Javassist와 AOP의 연동

Javassist는 AOP를 구현하는 데 매우 유용한 도구입니다. AOP의 핵심 원리는 프로그램의 핵심 비즈니스 로직과 관심사를 분리하는 것입니다. Javassist를 사용하면 프로그램의 클래스 파일을 동적으로 수정하므로, AOP를 구현할 때 필요한 핵심 비즈니스 로직에 코드를 주입하거나, 관심사를 제어하는 코드를 주입할 수 있습니다.

예를 들어, 메서드 호출 시간을 측정하는 로깅 관심사를 구현하고자 한다면, Javassist를 사용하여 모든 메서드 호출 시에 해당하는 코드를 주입할 수 있습니다.

아래는 Javassist를 사용하여 메서드 호출 시간을 측정하는 예제 코드입니다.

```java
import javassist.*;

public class MethodCallTimer {
  public static void main(String[] args) {
    try {
      // 클래스 파일 로드
      ClassPool pool = ClassPool.getDefault();
      CtClass cc = pool.get("target.ClassName");

      // 모든 메서드에 코드 주입
      for (CtMethod method : cc.getDeclaredMethods()) {
        method.insertBefore("long startTime = System.nanoTime();");
        method.insertAfter("long endTime = System.nanoTime();");
        method.insertAfter("System.out.println(\"메서드 실행 시간: \" + (endTime - startTime) + \"ns\");");
      }

      // 변경된 클래스 파일 저장
      cc.writeFile();
      cc.detach();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

위의 예제 코드에서는 Javassist를 사용하여 "target.ClassName" 클래스 파일의 모든 메서드에 코드를 주입합니다. 주입된 코드는 메서드 실행 전에 시작 시간을 기록하고, 실행 후에 종료 시간을 기록하며, 실행 시간을 출력합니다.

## 마무리

이번 포스트에서는 Javassist와 AOP를 소개하고, Javassist를 사용하여 AOP를 구현하는 예제 코드를 살펴보았습니다. Javassist는 바이트 코드를 동적으로 조작할 수 있는 강력한 도구이므로, 프로그램의 핵심 비즈니스 로직과 관심사를 분리하여 보다 모듈화된 소프트웨어를 개발할 수 있습니다.

더 많은 정보는 [Javassist 공식 웹사이트](https://www.javassist.org/)에서 확인할 수 있습니다.

Happy coding!