---
layout: post
title: "보일러 플레이트 코드 ( Boilerplate code ) 란?" 
date: 2020-04-09 10:12
description: "웹 개발 쪽을 하다 보니 여기선 개발을 시작할 수 있는 기초가 되는 주춧돌, template을 boilerplate라고 부르더라. boilerplate이 뭐냐면, "
date: 2020-04-09 10:15
tags: [programing]
comments: true
share: true
---

웹 개발 쪽을 하다 보니 여기선 개발을 시작할 수 있는 기초가 되는 주춧돌, template을 boilerplate라고 부르더라. boilerplate이 뭐냐면,  

> [정보기술](http://www.terms.co.kr/IT.htm)에서 말하는 보일러 플레이트는 변경 없이 계속하여 재 사용할 수 있는 저작품을 말한다. 확대 해석하면, 이 아이디어는 때로 "보일러 플레이트 코드"라고 부르는, 재사용 가능한 [프로그램](http://www.terms.co.kr/program.htm)을 가리키는 데 사용되기도 한다. 이 용어는 철강 제조 부문에서 유래되었으며, 보일러 플레이트는 원래 증기 보일러 내에 사용되는 커다란 압연 강판을 의미한다. 이 용어는 보일러 플레이트가 오랜 기간 동안 시험되었으며, 강철처럼 튼튼하다, 또는 반복적으로 재사용하기에 충분할 정도로 강력한 어떤 물건으로 만들어졌다는 등의 여러 가지 함축적인 의미를 내포하고 있다. [소프트웨어](http://www.terms.co.kr/software.htm)와 [하드웨어](http://www.terms.co.kr/hardware.htm)에 관한 계약 조건이 담겨 있는 법적 계약 등에서도 보일러 플레이트를 많이 사용한다. 이 용어는 또한 "보일러 플레이트 단락" 또는 "전체 문서는 보일러 플레이트였다" 등과 같이 형용사적으로 사용되기도 한다.  
> - 출처: www.terms.co.kr

  

예를 들어 React라는 기술을 이용해서 웹 프런트를 그린다면, javscript 의 최신 문법을 모든 브라우저들이 이해하지 못할 수 있기에 transpile (일종의 번역) 과정을 거쳐야 한다. 이를 위해 요즘은 webpack이라는 configuration library를 많이 쓰는데 초보자가 이 부분을 처음부터 건드리기엔 부담이 된다. 실제로 코딩 부트캠프에서 개발환경만 3일 동안 구축하다가 포기한 적이 있었다. 이런 상황에서 우린 빨리 개발해서 웹에 서비스를 올려서 보고 싶은데, 바로 시작할 수 있는 템플릿 코드 환경을 주는 것이라고 보면 된다.

  

아래는 facebook에서 관리하는, 가장 많이 쓰이는 React Boilerplate code이다.

[https://github.com/facebookincubator/create-react-app](https://github.com/facebookincubator/create-react-app)

[](https://github.com/facebookincubator/create-react-app)

**facebookincubator/create-react-app**

create-react-app - Create React apps with no build configuration.

github.com

  

이 코드를 깔면 바로 개발을 시작할 수 있다. 거짓말이 아니다. 정말 바로. 복잡한 설정 같은 부분도, 초심자가 건들 필요가 없다고 생각하는 부분들은 모두 hide처리 해 버렸다. 실제로 webpack.config 같은 파일은 당장은 건들 수 없게 되어있다. (물론 eject라는 명령어로 꺼내버릴 수도 있다. 그럼 조금 무서운 코드들이 밖으로 빠져나와 버린다. 복잡한 설정을 할 거가 아니라면 비추...)

  

개인적으로 생각할 때, 보일러 플레이트에서 얻을 수 있는 이점은, webpack과 같은 복잡한 configuration이나 folder structure 같은 부분이라고 생각한다. 처음에 code architecture를 초보자가 알 리가 없다. 그러면 보통 하나의 파일에 최대한 많이 때려 박기 시작하는데, 이러면 나중에 버그 잡기도 어렵고 코드 버전 관리하기도 거의 불가능해진다. 보일러 플레이트는 초보자에게 코드를 나누는 insight을 주는 것 같다. 프로젝트를 한 번 돌면 왜 폴더를 그렇게 나누고, 왜 코드를 그렇게 나누었는지 좀 알게 된다.

![](https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/1bqo/image/YIHbL64_eJcsP8s89FmGWGV0dfY.png)webpack 에서 bable-loader는 jsx 코드를 브라우저가 이해라 수 있는 js 코드로 transpile 을 해 준다

  

지난 프로젝트에서 내가 웹 프런트를 맡았을 때 힘겨웠던 점은 몇 가지가 있었다.

  

**1. test script 없이 매 번 테스트를 직접 해야 하는 번거로움**

이게 진짜, 막노동이 따로 없었다. 버그를 잡기 위해 몇 번이고 똑같은 절차적인 과정을 반복해야 했다. mocha 등을 사용해서 test case를 만들어 놓으면 자동으로 수십 가지의, 혹은 몇 가지만 test를 편하게 돌릴 수 있을 것 같은데 이번엔 반드시 적용해야겠다. unit test와 뭔가 순차적인 procedural test가 있을 것 같은데 순차적인 test는 어떻게 짜는지 더 알아봐야겠다. 그런데 예전에 듣기로 어떤 test는 결국 그냥 user가 하는 대로 하는 수밖에 없는 경우도 있으며, 또한 마지막으론 결국 user의 UI를 고려해야 하기에 무조건 해야 하는 테스트라고 들었다. 어찌 됐든 mocha/chai 등을 이용한 test case는 개발 시간을 40%는 줄여줄 것 같다.

  

**2. React Rendering을 매 번 browser refresh (F5) 해야 하는 번거로움**

server code나 React Client code를 변경하고 저장할 때마다 가장 번거로운 것은 다시 또 build를 하고 서버를 켜야 한다는 것이다. 처음 프로젝트에선 별다른 보일러 플레이트를 사용 안 했기에 매 번 브라우저를 새로고침 해야 하는 극악한 상황이었다. "꼭 이렇게 해야 하나?"라는 말을 파트너에게 거짓말 안 하고 200번은 했던 것 같다. 그다음 프로젝트에선 프런트 팀이 React-Hot-Loader를 적용해서 코드가 바뀔 때마다 브라우저가 자동으로 새로고침을 했다. webpack-dev-server를 사용했던 것으로 보인다. node-server 외에 server가 개발용으로 하나 더 있어서, client code를 감시하고 있다가 변화가 생기면 바로 build 해서 브라우저를 새 로고 침하는 형태인 것 같다. 엄청나게 개발 시간을 줄여줬지만, 그래도 불편했던 것은 브라우저가 새로고침이 되면 reloading 되는 게 꽤나 시간이 걸렸다. 그래서 최근 발견한 것은 HMR(Hot Module Replacement)라고 해서 브라우저 전체를 refresh 하는 것이 아니라 AJAX 통신할 때처럼, 바뀐 component부분만 re-rendering 하는 콘셉트이었다. 실제 적용해보니 환상적으로 편하고 빨랐다. 다만, React State 관련해서 몇 가지 주의해야 할 점이 있다고 하는데 좀 더 살펴봐야겠다. (Re-render 시, 특정 케이스의 state가 업데이트 안 된다던지) 아니면 그런 상황이 의심되면 그냥 브라우저 새로고침을 하면 된다.

  

  

문제는 내가 딱 원하는 구성의 보일러 플레이트를 찾기 어렵다는 것이다. 혹은, 있어도 너무 무겁고 거대한 보일러 플레이트인지라, 그 내부 구성을 잘 이해하기 어려운 경우도 있다. react-starter-kit이라고 있는데, 이건 정말 무시무시한 보일러 플레이트다. 대충 모든 기능들이 다 들어있다. 몇 번 시도해보다가, 내부 구조가 너무 복잡하게, 혹은 너무 최적화되어있어 빨리 판단을 내렸다. 이미 다 되어있어서 쓰기엔 편하지만, 혹시라도 어떤 문제가 생기거나, 추가 기능을 붙이고 싶을 때, 내부 코드 동작을 모르기 때문에 디버깅이 어려울 것 같다는 판단이었다.

  

굉장히 많은 기능이 담겨있는 무시무시한 React 보일러 플레이트 React Starter Kit

[https://github.com/kriasoft/react-starter-kit](https://github.com/kriasoft/react-starter-kit)

[](https://github.com/kriasoft/react-starter-kit)

**kriasoft/react-starter-kit**

react-starter-kit - React Starter Kit — isomorphic web app boilerplate (Node.js, Express, GraphQL, React.js, Babel, PostCSS, Webpack, Browsersync)

github.com

![](https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/1bqo/image/ho4FU-VvstLe-W4KTApuBw3dpPE.png)

  

아, 이럴 바에야 그냥 scratch부터 시작하자. 그래서 그냥 Udemy 강좌를 통해 webpack configuration을 배웠다. 막상 배우고 나니, 괴물같이 보였던 webpack이 조금은 친근하게 느껴졌다.

  

그럼에도 불구하고 시간을 절약하기 위해 가장 기본적으로 동작되는 boilerplate 몇 개를 결합해서 build에 문제가 없도록 조합했다. 그중에 가장 도움이 되었던 코드는 velopert님의 React-HMR 코드다. Velopert 님은 한국에서 React 쪽으로는 가장 초심자에게 쉽게 설명을 잘 해주고 있는 블로거다. 따로 동영상 강좌 및 live coding도 하시는데 정말 정성과 노력이 대단하시다. 코딩 센스도 일품이신 듯.. 블로그로 퀄리티 있는 강좌를 계속 올리니 출판사에서 연라도 왔다고 한다. 개발자라 한다면 어느 분야에나 따로 시간을 내서 일반적인 글이 되었던, 강좌가 되었든 올리고 다른 사람들과 소통하는 게 자신의 성장에 크게 도움이 되는 것 같다. 물론, 취업 시, 아니면 다른 사람과 팀 빌딩 시 이보다 더 큰 레퍼런스가 없을 것이다. 내가 팀빌딩을 할 수 있는 상황이고, 회사의 장래가 탄탄하다면 이런 귀한 인재분을 영입하기 위해 별 짓을 다할 것 같다. (결국 앞으로 해야 할 일 중 가장 중요한 사항일 듯)

[https://velopert.com/1492](https://velopert.com/1492)

[](https://velopert.com/1492)

**[React.JS] 강좌 11편 Express.js 서버 + 개발 서버 Hot Module Replacement 사용하기 | VELOPERT.LOG**

velopert.com

  

보일러 플레이트를 사용하건 아니건, 그건 중요하지 않은 것 같다. 다만, 최소한 기본적으로 이 코드가 어떻게 돌아가는지 알고 있어야 문제가 생겼을 때, 어디서 디버깅을 하면 되는지 감을 잡을 수 있기에 개발 시간을 지킬 수 있거나 아니면 개고생의 여지가 줄어들 것 같다. 정말, 문제는 다른 곳에 있는데, 잘 돌고 있는 코드에서 디버깅을 몇 시간, 며칠을 하기 일쑤다. 그러다가 다른 곳에서 해결이 되어 문제가 해결되면 배우기라도 하지, 가끔은 에러를 해결했는데 정확히 무슨 문제로 버그가 발생했는지, 어쩌다 에러는 해결됐고, 에러의 근본적인 원인은 그냥 지나칠 수 있기 때문이다.