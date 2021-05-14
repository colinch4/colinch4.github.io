---
layout: post
title: "[lib] Alamofire란?"
description: " "
date: 2021-05-14
tags: [lib]
comments: true
share: true
---


# Alamofire

## Alamofire란?
- Alamofire는 iOS, macOS를 위한 스위프트 기반 Http 네트워킹 라이브러리로 Apple의 Foundation networking 기반으로 인터페이스를 제공하여 일반적인 네트워킹 작업을 단순화한다.    

## 특징
- Request & Response의 체이닝 함수 제공      
- URL / JSON 형태의 파라미터 인코딩     
- File / Data / Stream / MultipartFormData 등 업로드 기능   
- HTTP Respones의 검증(Validation)       
--- 

## 기본 사용법     
```swift
Alamofire.request() //다른 모든 HTTP 요청은 파일 전송과 관련 없다
Alamofire.uplod() //multipart, stream, file, data method를 사용하여 파일을 업로드
Alamofire.download() //파일을 다운로드 하거나 이미 진행중인 다운로드를 다시 시작합니다
```

## Request
- Request란, 이름 그대로 요청을 보내기 위해 사용하는 함수이다.   
- Alamofire에는 HTTPMethod 라는 열거형이 정의되어 있다.   
![f1](https://user-images.githubusercontent.com/45002556/108619581-1ead6400-7469-11eb-8af6-140302199032.png)
- 대표적인 method는 REST API에서 이용되는 get, post, put, delete를 인자로 전달할 수 있으며 사용은 아래와 같이 한다. get 메소드가 default기 때문에 get 메소드 사용시에는 따로 method 인자를 전달하지 않는다.    
![f2](https://user-images.githubusercontent.com/45002556/108619583-20772780-7469-11eb-8430-386538aa87f7.png)
- request의 파라미터   
![f3](https://user-images.githubusercontent.com/45002556/108619585-210fbe00-7469-11eb-9a7c-a32081ceadc3.png)    
## URL 요청 예시	
![f4](https://user-images.githubusercontent.com/45002556/108619586-21a85480-7469-11eb-9aca-4cba56424ec5.png)
## 정리
- Alamofire란 iOS, macOS를 위한 Swift 기반의 HTTP 네트워킹 라이브러리이다
- Alamofire는 URLSession 기반이며 URLSession은 네트워킹 호출에서 모호한 부분이 많은데 Alamofire를 사용한다면 데이터를 접근하기 위한 노력을 줄일 수 있으면 코드를 더 깔끔하고 가독성 있게 쓰는 것이 가능하다


## Alamofire git 주소
<img width="438" alt="스크린샷 2021-03-01 오후 5 41 05" src="https://user-images.githubusercontent.com/45002556/109472339-534a9c80-7ab5-11eb-9d85-fb194270e8e6.png">

https://github.com/Alamofire/Alamofire
