---
layout: post
title: "[java] @NoArgsConstructor와 @AllArgsConstructor 어노테이션의 차이점은 무엇인가요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

- `@NoArgsConstructor`: 이 어노테이션은 인자를 받지 않는 기본 생성자를 자동으로 생성합니다. 이는 클래스의 객체를 인스턴스화 할 때 인자를 전달하지 않고도 객체를 생성할 수 있도록 합니다.

- `@AllArgsConstructor`: 이 어노테이션은 모든 필드를 인자로 받는 생성자를 자동으로 생성합니다. 이는 클래스의 객체를 인스턴스화 할 때 모든 필드에 대한 값을 전달하여 객체를 생성할 수 있도록 합니다.

따라서, `@NoArgsConstructor`는 인자 없이 객체를 생성하고 싶을 때 유용하며, `@AllArgsConstructor`는 모든 필드에 대한 값을 받아 객체를 생성하고 싶을 때 유용합니다.

이러한 어노테이션들은 객체 지향 프로그래밍에서 생성자 작성에 필수적인 작업들을 간편하게 처리해주는 편리한 도구로 사용될 수 있습니다.

참고 자료:
- [Lombok - @NoArgsConstructor](https://projectlombok.org/features/constructor)
- [Lombok - @AllArgsConstructor](https://projectlombok.org/features/constructor)