---
layout: post
title: "[네트워크] hashChange, pushState 차이"
description: " "
date: 2021-06-28
tags: [network]
comments: true
share: true
---


## hashChange, pushState 차이

웹팩으로 SPA 프로젝트를 만드는 과정에서 라우터를 구성할 때 hashChange, pushState 중 어떤 것을 사용할지 고민하다가 정리해보려고 한다.

pushState는 모든 주요 브라우저를 지원한다. history.js 등등이 폴리필의 역할을 하여 예전 브라우저들을 커버시켜주지만 모든 브라우저에서 전부다 사용할 수 있지는 않다.

pushState와 hashChange는 표면상으로 보이는 방법이 다르고 그 둘은 다른 방식으로 일을 처리한다. 이 두 부분은 굉장히 중요하다.

pushState는 당신의 사이트에서 가짜 네비게이션을 사용하기에 간단하고 깔끔하다. 예를들어 깃헙같은 경우엔 pushState를 사용해서 모든 네비게이션을 안보이게 하는데, 이를테면 어떤 링크를 클릭했을 때 JS가 이를 캐치하여 AJAX 요청을 보내고 새로운 페이지 컨텐츠를 로딩없이 업데이트한다. 주소창(location bar)는 업데이트된 컨텐츠와 매치되는 URL을 표시함은 물론이다. 이런 부분이 pushState의 용도이다.

pushState를 위와 같이 사용하는 경우 주소창의 링크는 진짜 컨텐츠를 나타내는 진짜 주소이다. 즉 그 주소로 페이지를 방문했을 때 MVC 아키텍쳐의 흐름과 같이 해당 페이지가 나타날 것이다. 중요한 점은 이 pushState의 네비게이션 기능은 꼭 필요로 하는 기능은 아니지만 사용자의 경험상으로는 필요한 부분이 많고, 이미 많은 어플리케이션에서 이를 적용하고 있다.

만약 MVC 프레임워크를 사용하지않고 단순 SPA만을 겨냥하는 상태라면, 즉 컨텐츠는 오직 JS를 통해서만 검색되고 서버가 이를 제어하지 않는 상태라고 가정하자.

이때 해시 URL을 통해 pushState를 사용하는 경우 브라우저의 URL이 실제 URL이 아닌 경우를 처리해야한다.

유저가 spa앱을 `http://mysite/mainpage`로 로드했다고 가정하자. 현재 주소창에는 위 주소가 떠있을 것이고 이는 진짜 주소이다. 이때 해시 URL을 사용하면 어떤 행동이 생겼을 때 `http://mysite/mainpage#charts/1`로 작동할 것이고,
pushState를 활용하면 `http://mysite/mainpage/charts/1`와 같이 주소 창에 보이게 될 것이다.

pushState만 사용한다면 이는 진짜 컨텐츠를 표시할 수 있는 링크가 될 수 없다. 물론 브라우저에서의 앞, 뒤 버튼은 잘 동작하겠지만 컨텐츠를 제대로 보이기 위해서는 server단의 처리를 통하여 표시해낼 수 있다. 즉 위와 같은 URL이라면 실제 URL을 확인하고 mainpage로 리다이렉트하고 의도한 페이지를 보여주는 과정이 필요하단 뜻이다.

그와 반대로 hashUrl을 사용하면 `http://mysite/mainpage#/charts/1`의 주소에서 브라우저는 onePage만 있다는걸 인지하고 유효한 url로 작동하기 때문에 사용자의 상호작용에 무리없이 대응할 수 있다. 여기에는 위와 같은 server측의 처리가 필요하지 않다.

pushState와 hash는 상호 배타적이지 않지만 보통 개발자는 둘 중 하나의 api만 사용하여 라우터를 만든다. 하지만 pushState는 단순히 유저에게 보이는 주소 표시와 안정적인 앞 뒤 네비게이션 역할만을 주로 하는 API일 뿐이다.

두 개 중 어떤걸 사용해야 하냐에 대한 정확한 답은 당연히 개발자가 어떤 서비스를 하고 이에 적합하느냐겠지만, 만약 개발자가 진짜 url 요청에 따라 server에서 처리하여 적합한 컨텐츠를 보이는 환경이라면 pushState만 사용해도 가능하다. 하지만 SPA라면 pushState 기반의 라우팅 보다는 hash를 활용하는게 전반적으로(구글봇에 의한 SEO 포함) 좋을 것이다. 물론 여기에 pushState를 사용하여 앞, 뒤 버튼을 통한 사용자 경험 최적화를 신경써주는 것이 가장 베스트일 것이다.

간단하게 정리하면 클라이언트에서만 사용하기 위해선 hash가 적합하고 상용 어플리케이션을 위해서는 pushState를 사용하는 것이 적합하다. 아무래도 기존 url형식을 차용해서 사용하는 부분 때문이다.

참조:
https://stackoverflow.com/questions/9340121/what-are-the-differences-between-history-pushstate-location-hash
https://developer.mozilla.org/ko/docs/Web/API/History/replaceState
https://developer.mozilla.org/ko/docs/Web/API/WindowEventHandlers/onhashchange
