---
layout: post
title: "[springcore] 빈 스코프"
description: " "
date: 2021-06-18
tags: [springcore]
comments: true
share: true
---

# 빈 스코프
- 싱글톤 : 객체 하나만 생성 (기본값)
- 프로토 타입 : 매번 객체 생성
	- Request
	- Session
	- WebSocket
	- 등등
```java
@Component @Scope("prototype")
```
- 프로토 타입 빈이 싱글톤 빈 참조하면? 상관없음
- 싱글톤 빈이 프로토타입 빈을 참조하면?
	- 프로토타입 빈이 업데이트 안됨
	- 업데이트 하려면
		- scoped-proxy
		```java
		@Component @Scope("prototype", proxyMode = ScopedProxyMode.TARGET_CLASS)
		```
		- Object-Provider
		```java
		@Component
		public class single {
			@Autowired
			ObjectProvider<Proto> proto;

			public Proto getProto() {
				return proto.getIfAvailable();
			}
		}
		```
		- Provider (표준)

- 프록시 패턴?
	- 여기서는 Proto타입 빈을 Proxy로 감싸 제공
	- 싱글톤안의 프로토타입 빈을 매번 변경시키기 위해 프록시로 감싸는 행위를 함

- 싱글톤 객체 사용시 주의할 점
	- 프로퍼티가 공유됨
	- ApplicationContext 초기 구동시 인스턴스 생성 