---
layout: post
title: "[javascript] Backbone.js에서 무한 스크롤(Infinite Scroll) 구현 방법"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

Backbone.js는 웹 애플리케이션 개발을 위한 자바스크립트 프레임워크로, 모델과 뷰를 효과적으로 관리할 수 있습니다. 이번 포스트에서는 Backbone.js를 사용하여 무한 스크롤(Infinite Scroll)을 구현하는 방법에 대해 알아보겠습니다.

## 1. 기본 설정

무한 스크롤을 구현하기 위해 다음의 기본 설정을 해야합니다.

### 1.1 컨테이너 요소 준비

무한 스크롤을 적용할 컨테이너 요소를 HTML 문서에 추가합니다. 이 요소는 스크롤 이벤트가 발생하는 영역으로 사용됩니다.

```html
<div id="scroll-container">
  <!-- 무한 스크롤될 내용 -->
</div>
```

### 1.2 필요한 모델과 컬렉션 생성

무한 스크롤을 위해 필요한 모델과 컬렉션을 Backbone.js에서 생성합니다. 이 모델과 컬렉션은 서버와의 데이터 통신에 사용됩니다.

```javascript
var Item = Backbone.Model.extend({
  // 모델 정의
});

var Items = Backbone.Collection.extend({
  model: Item,
  url: '/api/items' // 서버 API URL
});
```

## 2. 무한 스크롤 구현하기

### 2.1 스크롤 이벤트 감지

무한 스크롤을 구현하기 위해 컨테이너 요소에서 스크롤 이벤트를 감지해야 합니다. 이벤트를 감지하려면 Backbone.js의 `events` 객체를 사용합니다.

```javascript
var ScrollContainerView = Backbone.View.extend({
  el: '#scroll-container',
  
  events: {
    'scroll': 'loadNextPage'
  },
  
  loadNextPage: function() {
    // 다음 페이지의 아이템을 로드하는 로직 구현
  }
});
```

### 2.2 다음 페이지 아이템 로드

`loadNextPage` 메소드에서는 다음 페이지의 아이템을 로드하는 로직을 구현해야 합니다. 이를 위해 컬렉션의 `fetch` 메소드를 사용합니다.

```javascript
var ScrollContainerView = Backbone.View.extend({
  // 이전 코드 생략
  
  loadNextPage: function() {
    if (this.$el.scrollTop() + this.$el.innerHeight() >= this.$el[0].scrollHeight) {
      // 스크롤이 가장 아래 도달하면 다음 페이지 로딩
      items.fetch({ 
        data: { page: items.length / 10 }, 
        remove: false 
      });
    }
  }
});
```

위의 코드에서 `items`는 위에서 생성한 컬렉션 객체입니다. `data` 옵션을 사용하여 페이지 번호를 서버로 전달하고, `remove` 옵션을 `false`로 설정하여 기존 아이템을 유지하도록 합니다.

### 2.3 렌더링

마지막으로 무한 스크롤이 적용된 컨테이너 뷰에서 아이템을 렌더링하는 코드를 추가해야 합니다. 이를 위해 Backbone.js의 `listenTo` 메소드를 사용하여 컬렉션의 `add` 이벤트를 감지합니다.

```javascript
var ScrollContainerView = Backbone.View.extend({
  // 이전 코드 생략
  
  initialize: function() {
    this.listenTo(items, 'add', this.renderItem);
  },
  
  renderItem: function(item) {
    // 아이템을 렌더링하는 로직 구현
  }
});
```

위의 코드에서 `renderItem` 메소드는 새로운 아이템이 컬렉션에 추가될 때 호출되며, 이를 활용하여 아이템을 렌더링합니다.

## 3. 마치며

이번 포스트에서는 Backbone.js를 사용하여 무한 스크롤을 구현하는 방법에 대해 알아보았습니다. 스크롤 이벤트 감지, 다음 페이지 아이템 로드, 그리고 아이템 렌더링을 위한 간단한 코드를 작성하여 무한 스크롤을 구현할 수 있습니다. 이를 활용하여 웹 애플리케이션의 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [Backbone.js 공식 문서](http://backbonejs.org/)
- [Underscore.js 공식 문서](https://underscorejs.org/)