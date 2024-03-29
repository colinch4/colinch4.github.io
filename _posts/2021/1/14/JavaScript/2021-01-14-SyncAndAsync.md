---
layout: post
title: "[javascript] Sync / Async @JavaScript"
description: " "
date: 2021-01-14
tags: [javascript]
comments: true
share: true
---


## Sync / Async @JavaScript

Node.js는 대체로 코드를 실행시킬 때 비동기적으로 실행시키는 것을 권장한다. 따라서 동기적, 비동기적 프로그래밍이 뭔지 짚고 넘어갈 필요가 있다.

요약하자면 동기적 방식은 다수의 작업을 하나하나 완료될때까지 기다리며 차근차근 작업을 처리하는 것이고 (N번째 작업이 완전히 끝나야 N+1번째 작업이 시작됨), 비동기적 방식은 각각의 작업이 완료될때까지 기다리는게 아니라 동시에 모두 실행시켜 끝나는 순서대로 결과가 출력된다.

실생활에 비유해보자. 현재 청소(1시간), 빨래(2시간), 설거지(30분) 를 각각의 대행 업체에게 맡긴다고 가정하자.<br>**동기적 방법** 으로 이 것들을 해야한다면, 처음 청소 대행업체를 불러 1시간 동안 청소를 하고, 그 후 빨래업체를 불러 2시간 동안 빨래를 하며, 빨래가 끝난 후 설거지 업체에게 전화해 30분간 설거지를 한다.<br> 반면 비동기적 방식으로 이 것들을 한다면, 청소업체, 빨래업체, 설거지업체에게 차례로 전화를 걸어 일을 동시에 시키고 각각의 일이 끝나는대로 끝났다는 연락을 받는다. 

동기적 방식은 당연히 작업을 시작한 순서인 청소-빨래-설거지 순으로 작업이 끝나겠지만, 비동기적 방식은 작업이 걸리는 시간 순인 설거지-청소-빨래 순으로 작업이 끝날 것이다.

비동기적인 기술이 적용된 사례로는 대표적으로 메일전송이 있다. <br>네이버 메일을 켜 메일을 작성하고 보내기 버튼을 누르면, 바로 페이지가 바뀌며 전송완료 안내가 뜬다. 이는 정말로 메일 전송이 완료된 것이 아니라 (물론 속도가 빨라 거의 동시에 완료인 셈이지만..) 사용자가 다른 작업을 하기 위한 페이지 이탈을 못하고, 메일 전송 완료를 계속 기다리고 있어야 하는 불편함을 막기 위한 일종의 훼이크(?)다. 메일 전송 작업을 현재 메일 전송 페이지가 아닌 다른 프로그램에게 그 작업을 토스한 것이다. 그래서 유저는 메일 페이지에서 메일 전송 완료를 기다리지 않아도 백그라운드에서 네이버 자체 메일 전송 시스템이 메일을 보내준다. 이러한 방식 역시 비동기적 방식이다.



nodeJS의 API는 경우에 따라 동기 버전과 비동기 버전을 동시에 제공하기도 한다. Node.js의 API중 하나인 [fs.readFile](https://nodejs.org/dist/latest-v6.x/docs/api/fs.html#fs_fs_readfile_file_options_callback) 를 사용해 동기적 프로그래밍과 비동기적 프로그래밍의 예시를 살펴보자.

![https://drive.google.com/uc?id=0B3Or0Wv2t1xwdVpxU1FjZ0U1Nlk](https://drive.google.com/uc?id=0B3Or0Wv2t1xwdVpxU1FjZ0U1Nlk)

![https://drive.google.com/uc?id=0B3Or0Wv2t1xwZ0RjLWl3RUdxSUU](https://drive.google.com/uc?id=0B3Or0Wv2t1xwZ0RjLWl3RUdxSUU)

hello world!!! 가 적혀있는 data.txt를 읽어오는 작업이다. <br>코드의 순서대로 결과값이 출력되는 sync버전의 코드(4-6줄)와는 달리, Async (9-14줄)은 코드 작성 순서대로 결과값이 출력되지 않음을 알 수 있다. readFile 함수가 data.txt를 읽는 사이 다음 줄인 console.log(4); 가 먼저 실행되고 그 후 readFile함수가 일을 마치는 대로 이의 결과값이 출력된다.



### 참고 URL

[동기와 비동기 프로그래밍](https://opentutorials.org/course/2136/11884) ~~이고잉님 충성충성충성~~