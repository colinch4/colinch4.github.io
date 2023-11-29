---
layout: post
title: "[javascript] Marionette.js를 사용하여 반응형(Responsive) 레이아웃을 만드는 방법은 무엇인가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

반응형 웹 디자인은 모든 장치에서 웹 사이트 또는 애플리케이션이 적절하게 표시되도록하는 중요한 개념입니다. Marionette.js는 개발자들이 반응형 레이아웃을 만들기 위해 사용할 수 있는 강력한 도구이며, 이를 사용하는 방법에 대해 알아보겠습니다.

## 1. Marionette.Layout을 사용하여 레이아웃 구성
Marionette.js에서는 레이아웃을 구성하기 위해 `Marionette.Layout`을 사용할 수 있습니다. `Marionette.Layout`은 레이아웃을 정의하고 필요한 뷰를 렌더링하는 데 사용됩니다. 반응형 레이아웃을 만들기 위해 다양한 영역을 정의하고 알맞은 크기로 조정하는 것이 중요합니다.

```javascript
var MyApp = new Marionette.Application();

MyApp.addRegions({
  header: '#header',
  main: '#content',
  footer: '#footer'
});

MyApp.on('start', function() {
  var layout = new Marionette.Layout({
    template: '#layout-template',
    regions: {
      headerRegion: '#header',
      mainRegion: '#content',
      footerRegion: '#footer'
    }
  });

  MyApp.header.show(new MyHeaderView());
  MyApp.main.show(new MyMainView());
  MyApp.footer.show(new MyFooterView());
});

MyApp.start();
```

위의 코드 예제에서는 `Layout`을 정의하고 `header`, `main`, `footer`의 영역이 포함되었습니다. 각 영역은 해당하는 뷰로 렌더링되고, `show` 메서드를 사용하여 영역에 뷰를 표시할 수 있습니다.

## 2. CSS 미디어 쿼리를 사용하여 스타일 조정
반응형 레이아웃을 만들기 위해서는 CSS 미디어 쿼리를 사용하여 다양한 장치 및 화면 크기에 대해 스타일을 조정해야 합니다. Marionette.js를 사용하여 만든 레이아웃에 적절한 스타일을 적용하기 위해 미디어 쿼리를 사용할 수 있습니다.

```css
/* 스마트폰에 대한 스타일 */
@media (max-width: 600px) {
  #header {
    background-color: #f0f0f0;
    padding: 10px;
  }
  
  #content {
    font-size: 14px;
  }
  
  #footer {
    background-color: #f0f0f0;
    padding: 10px;
  }
}

/* 태블릿에 대한 스타일 */
@media (min-width: 601px) and (max-width: 1024px) {
  #header {
    background-color: #cccccc;
    padding: 20px;
  }
  
  #content {
    font-size: 16px;
  }
  
  #footer {
    background-color: #cccccc;
    padding: 20px;
  }
}

/* 데스크탑에 대한 스타일 */
@media (min-width: 1025px) {
  #header {
    background-color: #999999;
    padding: 30px;
  }
  
  #content {
    font-size: 18px;
  }
  
  #footer {
    background-color: #999999;
    padding: 30px;
  }
}
```

위의 CSS 코드 예제에서는 스마트폰, 태블릿, 데스크탑에 대한 스타일을 정의하는 미디어 쿼리를 사용하였습니다. 각 장치에 대해 다른 스타일을 적용하여 반응형 레이아웃을 만들 수 있습니다.

## 3. Resize 이벤트 처리
반응형 웹 애플리케이션에서는 윈도우 크기가 변경될 때 레이아웃을 조정하는 것이 중요합니다. Marionette.js에서는 `Marionette.Layout`에 `onRender` 메서드를 사용하여 윈도우의 `resize` 이벤트에 대한 처리 로직을 추가할 수 있습니다.

```javascript
var MyApp = new Marionette.Application();

MyApp.addRegions({
  header: '#header',
  main: '#content',
  footer: '#footer'
});

MyApp.module('LayoutModule', function(LayoutModule, MyApp, Backbone, Marionette, $, _) {

  LayoutModule.MyLayoutView = Marionette.LayoutView.extend({
    template: '#layout-template',
    regions: {
      headerRegion: '#header',
      mainRegion: '#content',
      footerRegion: '#footer'
    },
    onRender: function() {
      // 윈도우 크기 변경 이벤트에 대한 처리 로직 추가
      $(window).on('resize', _.debounce(this.onResize.bind(this), 200));
    },
    onResize: function() {
      // 레이아웃 크기를 조정하는 로직 구현
      var windowWidth = $(window).width();
      if (windowWidth < 600) {
        this.$el.addClass('small');
      } else {
        this.$el.removeClass('small');
      }
    }
  });
});

MyApp.on('start', function() {
  var layout = new MyApp.LayoutModule.MyLayoutView();

  MyApp.header.show(new MyHeaderView());
  MyApp.main.show(new MyMainView());
  MyApp.footer.show(new MyFooterView());

  MyApp.mainRegion.show(layout);
});

MyApp.start();
```

위의 코드 예제에서는 `onRender` 메서드를 사용하여 `resize` 이벤트에 대한 핸들러를 등록하고, `onResize` 메서드를 구현하여 레이아웃의 크기를 조정하고, 필요한 로직을 실행합니다.

## 결론
Marionette.js를 사용하여 반응형 레이아웃을 만들기 위해 `Marionette.Layout`을 사용하여 레이아웃 구성하고, CSS 미디어 쿼리를 사용하여 스타일을 조정하며, 윈도우의 `resize` 이벤트를 처리하는 방법을 살펴보았습니다. 이를 통해 다양한 장치의 화면에 적합한 반응형 레이아웃을 구성할 수 있습니다.

### 참조
- [Marionette.js 공식 사이트](https://marionettejs.com/)
- [CSS media queries - MDN web docs](https://developer.mozilla.org/ko/docs/Web/CSS/@media)
- [jQuery - resize event](https://api.jquery.com/resize/)