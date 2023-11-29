---
layout: post
title: "[javascript] Marionette.js에서 서버 사이드 렌더링(Server-side rendering)을 구현하는 방법은 무엇인가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

Marionette.js는 Backbone.js를 기반으로 한 JavaScript 애플리케이션 프레임워크로, 클라이언트 측에서 화면을 렌더링하는 것이 기본적인 사용 방법입니다. 하지만 때로는 서버 측에서도 화면을 구성하고 렌더링하는 것이 필요할 수 있습니다. 이를 위해 Marionette.js에서는 서버 사이드 렌더링을 지원하는 몇 가지 방법이 있습니다.

1. 텔레포팅(Teleporting): 텔레포팅은 Marionette.js에서 제공하는 기능으로, 클라이언트 측에서 렌더링된 뷰를 서버로 보내고, 서버에서 해당 뷰를 다시 렌더링하는 방식입니다. 클라이언트에서는 뷰를 렌더링한 후, 특정 요소(예: `<div>`)에 `data-view` 속성을 추가하고, 해당 요소와 함께 클라이언트에서 렌더링된 뷰 정보를 서버로 전송합니다. 서버는 받은 뷰 정보를 기반으로 해당 요소를 가져와 서버 사이드에서 렌더링을 수행합니다.

2. PhantomJS를 활용한 렌더링: PhantomJS는 Headless 브라우저로, Marionette.js 애플리케이션을 실행하고 렌더링할 수 있습니다. 서버 사이드 렌더링을 구현하기 위해, PhantomJS를 사용하여 Marionette.js 애플리케이션을 실행하고 웹 페이지를 완전히 렌더링하도록 할 수 있습니다. 이렇게 서버에서 완전한 렌더링된 페이지를 생성한 후, 해당 HTML을 클라이언트에 전송하여 화면에 표시할 수 있습니다.

3. Backbeat과의 통합: Backbeat은 Marionette.js와 함께 사용할 수 있는 서버 사이드 렌더링 프레임워크입니다. Backbeat은 Backbone.js와 호환되며, Marionette.js를 사용하는 애플리케이션의 서버 측에서 렌더링을 처리할 수 있도록 지원합니다. Backbeat을 사용하면 클라이언트와 서버 사이에서 모델 및 뷰를 공유하고, 서버에서 렌더링된 HTML을 생성하여 클라이언트에 전송할 수 있습니다.

Marionette.js에서 서버 사이드 렌더링을 구현하는 방법은 몇 가지가 있으며, 프로젝트의 요구사항에 따라 적절한 방법을 선택할 수 있습니다. 여러 가지 방법 중에서도 텔레포팅이나 PhantomJS를 사용하는 방법이 상대적으로 더 간단하고 직관적입니다. 요구사항이 복잡하거나 Marionette.js 애플리케이션을 사용자 정의해야 하는 경우 Backbeat을 사용하여 더 유연하고 확장 가능한 서버 사이드 렌더링을 구현할 수 있습니다.

참고 자료:
- [Marionette.js 공식 문서](https://marionettejs.com)
- [Backbeat 공식 GitHub 저장소](https://github.com/chaplinjs/backbeat)