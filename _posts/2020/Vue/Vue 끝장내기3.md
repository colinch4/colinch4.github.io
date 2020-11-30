---
layout: post
title: "Vue 끝장내기 3"
description: " "
date: 2020-11-16
tags: [vue]
comments: true
share: true
---

### Vue 강의 들으면서 내용 정리하기 !
- 추후 업데이트 할 예정
<hr/>

## 섹션15 : 학습 노트 데이터 수정

**🔎다이나믹 라우터 매칭**

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%EB%9D%BC%EC%9A%B0%ED%84%B0%20%EB%A7%A4%EC%B9%AD.png"/>
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EC%95%84%EC%9D%B4%EB%94%94%EC%97%B0%EA%B2%B0.png"  width="50%"> <img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/route%20id%20path%20%ED%99%95%EC%9D%B8.png" width="50%">

- route 에 path 를 정의할때 파라미터로 id를 받아서 해당 페이지로 진입했을때 그 아이디로 접근할 수 있는 형태

## 섹션16 : 데이터 포맷팅

**🔎VUe filter**
- [뷰 필터 안내 문서](https://vuejs.org/v2/guide/filters.html#ad)
<pre><code>
<--in mustaches-->
{{ message | capitalize }}
</pre></code>

- |(파이프) 를 이용해서 필터함수 이름만 넣어주게 되면 데이터에 필터함수의 내용을 결합하여 필터함수를 돌려서 나온 결과를 화면에 뿌려준다.

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/formatDate.png" width="70%">
- filter 적용방법
- 위와 같이 적용한다면 해당 컴포넌트에서만 사용 가능한 filter 이다.

#### 🤔만약 여러컴포넌트에서 이용하고 싶다면?
- **전역** 필터로 사용하면 된다!

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/utils%20filter.png" width="70%">

- utils > filter 

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/format%20main%20js.png" width="70%">

- main.js 에서 전역으로 연결

**앞으로도 특정 텍스트를 형식화할 일 이 있을때는 filter 기능 사용할 것!**



## 섹션17 : 라우터 심화


**🔎라우터 네비게이션 가드란?**
- [라우터 네비게이션 가드 문서](https://router.vuejs.org/guide/advanced/navigation-guards.html)
- 로그인하지 않은 사용자가 특정 url 페이지로 이동했을때 이동을 막는것. : router.beforeEach
- 특정 라우터에 진입 하기 전에 beforeEnter 와 같은 라우터네비게이션 가드를 이용해서 데이터 먼저 호출후 받아왔을때만 로딩하게 함.

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EB%9D%BC%EC%9A%B0%ED%84%B0%20%EB%84%A4%EB%B9%84%EA%B2%8C%EC%9D%B4%EC%85%98%EA%B0%80%EB%93%9C%20%EA%B8%B0%EC%B4%88%20%EC%BD%94%EB%93%9C.png" width="70%">

- new VueRouter 인스턴스가 router 변수에 담기게 끔 한다.
- export default 로 router 를 내보내야 한다.
- next 를 호출했을때만 beforeEach 의 특정로직 예를 들어 위와 같은 코드에서는 로그를 찍고 이동하는 로직을 확인 할 수있다.
- next 호출해줘야지만 다음페이지로 이동할 수 있다.

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/meta%20auth%20true.png" width="70%">
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/meta%20auth%20true%20if.png" width="70%">

- 라우터 페이지 속성에 meta 안에 auth 속성이 true 면 인증이 필요하다가 뜰 것.
- meta auth 를 통해 권한을 부여했다.
- meta auth true 를 이용해서 이 페이지는 권한이 필요하다까지 정의함.

**로그인 하지 않은 사용자를 인증이 필요한 페이지에 접근 할 수 없도록 라우터 네비게이션 가드 코드 추가**
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/meta%20auth%20store.getters.isLogin.png" width="70%">

**로그아웃 시 쿠키 지우는 코드**

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/appheader%20%ED%86%A0%ED%81%B0%20%EC%BF%A0%ED%82%A4%20%EC%82%AD%EC%A0%9C.png" width="70%">
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/store%20%ED%86%A0%ED%81%B0%EA%B0%92%20%EC%A7%80%EC%9A%B0%EA%B8%B0.png" width="50%">

- appheader 와 store 에 코드 수정
- store 에 토큰값을 지우는 코드를 추가해주고, utils/cookies.js 에 있는 { deleteCookie } 를 이용해서 appheader 에서 쿠키값을 지워준다.
- deleteCookie 에서는 til_auth & til_user 필요! 


## 섹션17 : 프런트엔드 테스팅 소개

**🔎**

<img watchall>
- jest(자바스크립트 테스팅이 기본적으로 jest 로 설정되어있음) 라는 도구에서 테스트 실행할때 watchall 이라는 옵션을 붙여서 테스트 코드파일이 변화됬을때마다 다시 자동으로 테스트 해주는 명령어

- components / LoginForm.spec.js 파일을 만들어주고 터미널을 열어서 npm t 를 해주면 테스트가 실행된다./ control + c 하면 꺼짐!

**테스트를 하는 목적?**
- 각 페이지마다 기능이 있는데, 직접 코드를 치지 않아도 기능이 잘 돌아간다는 보장을 테스트코드를 통해서 할 수 있게 된다.
- 일일이 기능을 손으로 확인하는 시간을 줄여준다.

**Jest**
- 페이스북이 개발한 자바스크립트의 테스팅 라이브러리
- [Jest 공식 사이트](https://jestjs.io/en/)
- vue cli 설치할때 test 를 설치했기 때문에 따로 설치하지 않아도 된다.
 
 <pre><code> ex ) package.json : "@vue/cli-plugin-unit-jest" , "@vue/test-utils" 를 확인할수있다.</pre></code> 
 
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/spec%20js.png" width="30%">

- 자바스크립트 파일에서 위와 같이 가운데에 spec 또는 test 가 붙는다면, 자바스크립트 테스트 파일.

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/jest%20testMatch.png" width="70%">

- jest.config 파일에서 testMatch 부분이 없다면, test 폴더를 따로 만들어서 그안에 넣어줘야한다.
- 하지만 위와 같이 코드를 작성하게 되면, 테스팅할 파일과 가장 가까운 위치에 위치하거나, __test__ 폴더를 만든 뒤 그 안에 넣어줄 수 있다.

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%BD%94%EB%93%9C%20%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0.png" width="70%">

- 간단하게 테스트코드를 작성해보았다.
- 테스트 코드를 작성할때는 기능이 깨지는 케이스에 대해서 먼저 점검하고 점차 줄여가는것이 좋다.
 <pre><code> ex ) expect(result).not.toBe(30);</pre></code> 
- 여기서 빨간줄이 뜨는 이유는 eslint 에서 jest 문법을 이해하지 못했기 때문 > eslintrc.js 에서 수정

 <pre><code>
  env: {
    node: true,
    jest: true
  },
  </pre></code>
  
  - env 부분에 jest 를 추가해 준다.
  
  **뷰 컴포넌트 테스트 방법**
  
  <img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/jest%20mount.png" width="70%">
  
  - jest 에서는 console.log 가 가능하다!
  
  **[Vue Test Utils 공식 문서](https://vue-test-utils.vuejs.org/guides/)**
  - Vue Test Utils : vue js 를 위한 유닛 테스팅 공식 라이브러리
  - vue cli 생성 했을떄 Vue Test Utils이라는 플러그인을 이미 선택했기때문에 import 해서 사용 가능.
  - 밑에 처럼 이용 👇👇
  
  <img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/vue-test%20util%20shallowMount.png" width="80%">
  
   <pre><code>
  describe('LoginForm.vue', () => {
  test('ID는 이메일 형식이어야 한다', () => {
    const wrapper = shallowMount(LoginForm);
    const idInput = wrapper.find('#username');
    console.log(idInput.html());
  });
});
 </pre></code>
 
 - .find() : vue/test-utils 에서 제공, LoginForm 이 화면에 부착됬을때 template 안에 있는 특정 html 요소를 쫓아갈 수 있는 api
 - 위와 같이 console.log(idInput.html()); 를 해준다면, 콘솔에 해당 html태그를 확인 할 수 있다.
 
 <img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B4%80%EC%A0%90%20%EC%95%84%EB%8B%8C%20%ED%85%8C%EC%8A%A4%ED%8A%B8.png" width="80%">

- 위와 같은 코드는 사용자 관점이 아닌 테스트 코드이다.
- 그렇다면 어떻게 사용자 관점의 코드를 쓸 수 있을까?

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/Vue/images/%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B4%80%EC%A0%901.png" width="80%">

 <pre><code>
 expect(button.element.disabled).toBeTruthy();
  // .toBeTruthy() : 앞에 있는 값이 true 인지 아닌지
  </pre></code>
  
  
