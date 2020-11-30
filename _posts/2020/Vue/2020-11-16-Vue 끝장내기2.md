---
layout: post
title: "Vue 끝장내기 2"
description: " "
date: 2020-11-16
tags: [vue]
comments: true
share: true
---

### Vue 강의 들으면서 내용 정리하기 !
- 추후 업데이트 할 예정
<hr/>

## 섹션10 : 브라우저 저장소를 이용한 인증값 관리

**🔎새로고침할때 문제점 해결하기**

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%ED%86%A0%ED%81%B0%EA%B0%92_%EC%9C%A0%EC%A0%80%EC%9D%B4%EB%A6%84%20%EC%A0%80%EC%9E%A5.png" width="90%" />
- 토큰저장하고, 라우터 저장할때 단순히 자바스크립트에 저장하는게 아니라 브라우저 저장소를 이용해서 토큰값을 저장하면 새로고침을 하더라도, 브라우저 저장소에서 토큰값을 꺼내와서 사용가능.

**이때 쿠키를 저장하는 방법 👇**

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EC%BF%A0%ED%82%A4%EC%A0%80%EC%9E%A5%ED%95%98%EB%8A%94%EB%B0%A9%EB%B2%95.png" width="90%"/>


**쿠키 패널에서 확인하는 방법**

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%ED%8C%A8%EB%84%90%EC%97%90%EC%84%9C%20%EC%BF%A0%ED%82%A4%EA%B0%92%20%ED%99%95%EC%9D%B8.png" width="450px"/>

- 하지만 이렇게 되어도 새로고침할땐 값이 리셋된다. 그 이유는 스토어에 값이 전달 되지 않았기 때문인데 그때 cookies 의 { getAuthFromCookie, getUserFromCookie } 를 사용한다


<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EC%BF%A0%ED%82%A4%EC%99%80%EC%8A%A4%ED%86%A0%EC%96%B4%EC%9D%98%EC%97%B0%EA%B2%B0.png" width="90%" />


**❗️❗️컴포넌트단의 무거운 비지니스 로직이 많이 노출되기 보다는 다른파일에 코드로 옮기는 것이 좋다** 

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/actions%20%EB%A1%9C%20%EB%84%98%EA%B8%B4%20%EC%BD%94%EB%93%9C.png" width="90%"/>

- store > index > actions 로 넘기는것이 좋다


<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/await-dispatch.png" width="90%" />

- index의 LOGIN 비동기처리 끝나고나면 라우더로 메인페이지로 진입을 하기 때문에 await 가 꼭 필요하다.

- await 를 빼게되면 순서처리가 맞지 않는다 

- 그 이유는 토큰을 받아서 스토어에 저장한 후 라우터로 진입을 해야하는데 await가 없으면 dispatch 가 끝나기도 전에 라우터에 진입하게 되서 비동기처리가 되지 않는다.

- **await 필수!!**


## 섹션12 : 중간정리
**🔎뷰 라우터 및 컴포넌트 설계**
- [코드스플리팅](https://github.com/jina95/TIL/blob/master/Vue/Vue%20%EB%81%9D%EC%9E%A5%EB%82%B4%EA%B8%B0.md)

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EC%BD%94%EB%93%9C%EC%8A%A4%ED%94%8C%EB%A6%AC%ED%8C%85.png" width="70%"/>

- 페이지 컴포넌트를 정의하는 것이 아니라, 화살표 함수에 import 조합을 해서 url을 요청하는 시점에 해당 자원을 서버에서 당겨온다.

**브라우저 저장소를 이용한 인증 값 관리**
- 쿠키와 로컬스토리지의 차이점은 ? 
- 쿠키는 토큰, 특정 값에 대한 만료기간을 설정가능 / 로컬스토리지는 설정 할 수 없다.


## 섹션13 : API 함수 모듈화
**인스턴스 생성 함수 분할**

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/api%20index%20%ED%95%A8%EC%88%98%EB%B6%84%ED%95%A0%20.png" width="90%" />

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/api%20index%20%20%ED%8C%8C%EC%9D%BC%20%EA%B5%AC%EC%A1%B0.png" width="300px" />

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%84%B1%EA%B2%A9%EB%B3%84%EB%A1%9C%20%EC%AA%BC%EA%B0%A0%20API.png" width="50%" />

- 하나의 파일에서 모든것을 관리하게 되면 실제로 작업할때 불편하게 된다.(실제로는 몇백줄이 되기 때문에)
- 따라서 모듈화를 이용, 인스턴스 조합으로 데이터 성격별로 파일을 쪼개는 것이 효율적





