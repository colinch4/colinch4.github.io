---
layout: post
title: "[springcore] Spring IoC컨테이너와 Bean"
description: " "
date: 2021-06-18
tags: [spring]
comments: true
share: true
---

## Spring IoC컨테이너와 Bean
- 의존 관계 주입
- 객체를 사용할 때 직접 만들어서 사용하는 것이 아니라, 주입 받아 사용하는 방법
- 최근에는 xml로 설정하는 것보다 자바 클래스로 설정파일을 생성하고, 객체 주입을 받을 때도 설정이나, 생성자를 이용하기보다 애노테이션을 많이 사용

## 스프링 IoC 컨테이너이란?
- BeanFactory
- 애플리케이션 컴포넌트의 중앙 저장소
- 빈 설정 소스로 부터 빈 정의를 읽어들이고, 빈을 구성하여 제공

## Bean이란?
- 스프링 IoC 컨테이너가 관리하는 객체
- 장점
	- Scope
		- 싱글톤 : 하나의 객체만 사용
		- 프로토타입 : 매번 다른 객체 생성
	- 라이프사이클 인터페이스 제공
		- @PostConstruct을 사용하면 빈 생성 이후의 작업을 정의할 수 있음
	- 의존성 주입 가능
		- 테스트 용이 (Mock객체를 생성하여 주입가능)
	```java
	...생략
	@Mock
	BookRepository bookRepository;

	@Test
	public void save() {
		Book book = new Book();

		when(bookRepository.save()).thenReturn(book);
		... 생략
	}
	```
	