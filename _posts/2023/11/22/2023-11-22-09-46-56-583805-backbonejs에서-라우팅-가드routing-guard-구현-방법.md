---
layout: post
title: "[javascript] Backbone.js에서 라우팅 가드(Routing Guard) 구현 방법"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

Backbone.js는 JavaScript로 구현된 웹 애플리케이션의 구조를 구축하기 위한 프런트엔드 프레임워크입니다. 이 프레임워크는 MVC (Model-View-Controller) 패턴을 기반으로 하며, 라우팅을 통해 화면 간의 이동을 관리합니다.

라우팅 가드(Routing Guard)는 사용자가 특정 화면으로 이동하기 전에 실행되는 함수로, 사용자의 권한이나 상태에 따라 화면 이동을 제한 또는 허용하는 역할을 합니다. 이 글에서는 Backbone.js에서 라우팅 가드를 구현하는 방법을 알아보겠습니다.

## 1. `Backbone.Router` 확장하기

라우터를 사용하여 애플리케이션의 라우팅을 정의할 수 있습니다. 가드를 구현하기 위해 `Backbone.Router` 클래스를 확장하고, `route` 메서드를 오버라이딩하여 가드 함수를 추가합니다.

```javascript
var AppRouter = Backbone.Router.extend({
    routes: {
        'dashboard': 'dashboard',
        'profile': 'profile'
    },

    route: function(route, name, callback) {
        var guardCallback = this.guardCallbackFactory(callback);
        return Backbone.Router.prototype.route.call(this, route, name, guardCallback);
    },

    guardCallbackFactory: function(callback) {
        var self = this;
        return function() {
            if (self.isAuthorized()) {
                callback.apply(self, arguments);
            } else {
                self.redirectToLogin();
            }
        };
    },

    isAuthorized: function() {
        // TODO: 권한 체크 로직 구현
    },

    redirectToLogin: function() {
        // TODO: 로그인 화면으로 리다이렉트
    },

    dashboard: function() {
        // TODO: 대시보드 화면 로직
    },

    profile: function() {
        // TODO: 프로필 화면 로직
    }
});
```

위 코드에서 `guardCallbackFactory` 메서드는 원래의 콜백 함수를 감싸는 가드 함수를 생성합니다. `isAuthorized` 메서드에서는 사용자의 권한을 체크하는 로직을 구현하고, 권한이 있는 경우 콜백을 실행하고 그렇지 않은 경우 로그인 화면으로 리다이렉트합니다.

## 2. 라우터 초기화 및 시작

라우터를 초기화하고 애플리케이션을 시작하는 부분에 아래와 같은 코드를 추가합니다.

```javascript
$(document).ready(function() {
    var router = new AppRouter();
    Backbone.history.start();
});
```

위 코드에서는 `AppRouter` 인스턴스를 만들고, `Backbone.history.start()`를 호출하여 브라우저의 URL에 따라 라우팅을 시작합니다.

## 마무리

위의 방법을 따라 Backbone.js 애플리케이션에 라우팅 가드를 구현할 수 있습니다. 사용자의 권한이나 상태에 따라 특정 화면으로의 접근을 제한하고, 필요에 따라 로그인 화면으로 이동할 수 있습니다.

라우팅 가드는 사용자 경험을 개선하고 보안을 강화하는 데 도움이 됩니다. Backbone.js에서 강력한 라우팅 가드를 구현하여 웹 애플리케이션의 안정성과 안전성을 높여보세요.

## 참고 자료
- [Backbone.js 공식 문서](https://backbonejs.org/)