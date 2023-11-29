---
layout: post
title: "[javascript] Marionette.js에서 사용되는 대화창(Dialog) 및 팝업창(Popup) 컴포넌트를 구현하는 방법은 어떤 것인가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

## Marionette.Dialog 컴포넌트

Dialog 컴포넌트는 사용자와의 상호작용을 위한 대화창을 생성하는 데 사용됩니다. Marionette.Dialog은 Marionette.View를 기반으로 작동하며, 기본적으로 모달(modal)창으로 구성됩니다. 아래는 Marionette.Dialog 컴포넌트를 구현하는 예시입니다.

```javascript
const MyDialog = Marionette.Dialog.extend({
  template: _.template('<h1>Dialog Title</h1><p>Dialog Content</p>'),
  onBeforeRender: function() {
    this.$el.addClass('my-dialog');
  },
  events: {
    'click .close': 'closeDialog'
  },
  closeDialog: function() {
    this.destroy();
  }
});

const dialog = new MyDialog();
dialog.render();
```

위의 예제에서는 MyDialog라는 사용자 정의 Dialog 컴포넌트를 정의하였습니다. `template` 속성을 통해 대화창에 표시될 HTML 마크업을 정의할 수 있습니다. `onBeforeRender` 메서드를 사용하여 Dialog 컴포넌트에 클래스를 추가하는 등의 초기화 작업을 수행할 수 있습니다. `events` 객체를 사용하여 사용자의 동작에 반응하는 이벤트 핸들러를 정의할 수 있습니다.

Dialog 컴포넌트를 생성한 후 `render()` 메서드를 호출하여 화면에 렌더링할 수 있습니다. 또한 필요에 따라 `closeDialog()` 메서드를 사용하여 Dialog 컴포넌트를 닫을 수 있습니다.

## Marionette.Popup 컴포넌트

Popup 컴포넌트는 Tooltip, Dropdown 메뉴 등과 같이 사용자의 특정 동작에 응답하여 임시적으로 표시되는 작은 창을 구현할 때 사용됩니다. Marionette.Popup은 Marionette.View를 상속받아 작성되며, 기본적으로 모달이 아닌 비 모달(non-modal)형태로 작동합니다. 아래는 Marionette.Popup 컴포넌트를 구현하는 예시입니다.

```javascript
const MyPopup = Marionette.Popup.extend({
  template: _.template('<p>Popup Content</p>'),
  onRender: function() {
    this.$el.addClass('my-popup');
  },
  hide: function() {
    this.destroy();
  }
});

const popup = new MyPopup();
popup.render();
```

위의 예제에서는 MyPopup이라는 사용자 정의 Popup 컴포넌트를 정의하였습니다. `template` 속성을 통해 Popup에 표시될 HTML 마크업을 정의할 수 있습니다. `onRender` 메서드를 사용하여 Popup 컴포넌트에 클래스를 추가하는 등의 초기화 작업을 수행할 수 있습니다.

Popup 컴포넌트를 생성한 후 `render()` 메서드를 호출하여 화면에 렌더링할 수 있습니다. 또한 필요에 따라 `hide()` 메서드를 사용하여 Popup 컴포넌트를 숨길 수 있습니다.

이렇게 Marionette.js에서 제공하는 Dialog 및 Popup 컴포넌트를 사용하면, 간편하게 대화창과 팝업창을 구현할 수 있습니다. Marionette.js의 공식 문서를 참조하여 더 자세한 사용법을 익히실 수 있습니다.

## 참고 자료

- [Marionette.js 공식 문서](https://marionettejs.com/docs/v4.5.1/)