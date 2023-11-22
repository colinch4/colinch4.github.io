---
layout: post
title: "[javascript] Backbone.js에서 이벤트 버블링(Event Bubbling) 처리 방법"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

Backbone.js는 JavaScript로 구현된 웹 애플리케이션 개발을 위한 프레임워크로서, 이벤트 기반 아키텍처를 지원합니다. 이벤트 버블링(Event Bubbling)은 자식 엘리먼트에서 발생한 이벤트가 부모 엘리먼트로 전달되는 동작을 말합니다. Backbone.js에서 이벤트 버블링을 처리하는 방법에 대해 알아보겠습니다.

## 이벤트 버블링 처리 방법

Backbone.js에서는 뷰(View)와 이벤트를 함께 사용하여 이벤트 핸들링을 처리합니다. 이벤트 버블링을 처리하기 위해서는 다음과 같은 방법을 사용할 수 있습니다.

1. 부모 뷰에 이벤트 핸들러를 등록하고, 해당 핸들러에서 자식 뷰로 이벤트를 전파시킵니다. 자식 뷰에서 발생한 이벤트를 부모 뷰는 자체적으로 처리할 수 있습니다.

```javascript
// 부모 뷰
var ParentView = Backbone.View.extend({
  events: {
    'customEvent': 'handleCustomEvent'
  },

  initialize: function() {
    // 자식 뷰 생성
    this.childView = new ChildView();
  },

  handleCustomEvent: function() {
    // 이벤트 처리 로직 작성
  }
});

// 자식 뷰
var ChildView = Backbone.View.extend({
  events: {
    'click': 'handleClick'
  },

  handleClick: function() {
    // 부모로 이벤트 전파
    this.trigger('customEvent');
  }
});
```

2. Backbone.js의 `listenTo` 메서드를 사용하여 부모 뷰와 자식 뷰 간의 이벤트를 연결할 수 있습니다.

```javascript
// 부모 뷰
var ParentView = Backbone.View.extend({
  initialize: function() {
    // 자식 뷰 생성
    this.childView = new ChildView();
    // 자식 뷰의 이벤트를 감지하여 핸들러 호출
    this.listenTo(this.childView, 'customEvent', this.handleCustomEvent);
  },

  handleCustomEvent: function() {
    // 이벤트 처리 로직 작성
  }
});

// 자식 뷰
var ChildView = Backbone.View.extend({
  events: {
    'click': 'handleClick'
  },

  handleClick: function() {
    // 부모로 이벤트 전파
    this.trigger('customEvent');
  }
});
```

3. 부모 뷰에서 `delegateEvents` 메서드를 오버라이드하여 서브뷰의 이벤트 처리를 직접 지정할 수 있습니다.

```javascript
// 부모 뷰
var ParentView = Backbone.View.extend({
  delegateEvents: function() {
    // 기존 이벤트 핸들러 제거
    this.$el.off('.delegateEvents' + this.cid);

    // 부모 뷰 이벤트 핸들러 등록
    this.$el.on('customEvent', this.handleCustomEvent);

    // 자식 뷰 이벤트 핸들러 등록
    this.childView.delegateEvents();
  },

  handleCustomEvent: function() {
    // 이벤트 처리 로직 작성
  }
});

// 자식 뷰
var ChildView = Backbone.View.extend({
  events: {
    'click': 'handleClick'
  },

  handleClick: function() {
    // 부모로 이벤트 전파
    this.parent.trigger('customEvent');
  }
});
```

## 결론

Backbone.js에서 이벤트 버블링을 처리하기 위해서는 부모 뷰와 자식 뷰 사이의 이벤트를 연결하고, 이벤트를 전파시키는 방법을 사용할 수 있습니다. 이를 통해 웹 애플리케이션에서 발생한 이벤트를 효율적으로 처리할 수 있습니다.

*참고 자료*
- [Backbone.js 공식 문서 (영문)](https://backbonejs.org/)
- [Backbone.js 이벤트 (영문)](https://backbonejs.org/#Events)