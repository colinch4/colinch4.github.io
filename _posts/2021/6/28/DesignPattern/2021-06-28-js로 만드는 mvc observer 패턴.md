---
layout: post
title: "[디자인패턴] js로 만드는 mvc+observer 패턴"
description: " "
date: 2021-06-28
tags: [디자인패턴]
comments: true
share: true
---

# js로 만드는 mvc+observer 패턴

기존 mvc 패턴은 view를 통해 컨트롤러로 들어온 Action에 따라 모델이 변경되고 이 변경된 모델은 컨트롤러를 통해 뷰를 변경시킨다.

MVC 모델은 layered style 이고 layered style에서는 아래 레이어는 상위 레이어를 사용하는 것을 권장하지 않는다.

a계층이 b계층을 사용하면 a계층은 b계층에 종속되고 b계층이 없으면 a계층은 자신의 역할을 수행할 수 없다. 이러한 관계를 `usage dependency`라고 한다. 즉 상위 계층은 하위계층에 대해 `usage dependency`가 있다.

하지만 하위 계층이 상위 계층에 있는 기능을 사용하면 하위 계층이 상위 계층에 종속되어버리는데 이때 mvc 모델에서 모델이 뷰의 기능을 사용하는 상황과 같이 볼 수 있다.

여기에 Observer 패턴을 적용시킨다면 모델은 "Observable"(관찰 가능 항목)이라 불릴 수 있고 view는 "Observer"라고 불릴 수 있다.

"Observable"이 변경되면 해당 상태를 관찰자에게 알리고 관찰자는 해당 변경사항에 대응할 수 있어야 한다. 이는 데이터 흐름을 단방향으로 만들고 컨트롤러는 더이상 뷰를 업데이트할 필요 없이 뷰는 모델을 따라서 업데이트가 되게 한다.

위와 같은 흐름은 어떤 객체에 상태에 변화가 생기면 그 객체의 상태에 관심있는 객체들에게 알려주는 흐름을 가지고 있다.

이 같이 모델에서 관심있는 객체들의 참조를 갖고 옵저버 인터페이스를 적용한 뷰 인스턴스들을 관리하는 방식은 인스턴스의 참조들만 가짐으로써 기존 mvc 모델에서 모델과 뷰의 결합도(coupling) 문제를 피해갈 수 있는 패턴이다.

<img src="https://miro.medium.com/max/906/1*m4GC21LL7em3t9jnbAlWgw.png">

모델에는 observable 인터페이스를 적용하고, 뷰에는 observer 인터페이스를 적용해야한다. 두 인터페이스는 DOM API를 통해 적용된 EventListener 인터페이스와는 달리 직접 추상화를 해야한다. 이 과정에서 만들어지는 메소드는 JAVA에서 정의된 인터페이스를 따르는 것이 유지보수의 관점에서 더 좋을 것이다.

<img src="https://miro.medium.com/max/854/1*mmTHcQFfbad820Dz75hHgQ.png">

모델 클래스에 `notifyAll` 메소드, 뷰 클래스에는 `update` 메소드를 추가한다. 그리고 모델클래스에는 `registerObserver` 메소드와 이 메소드를 통해 추가 될 `observer`의 참조들을 저장할 `observers`라는 배열을 하나 만들어준다.

그리고 모델과 뷰가 인스턴스화 될 때 우리는 `registerObserver` 메소드를 통해 뷰를 모델에 등록하고 이를 통해 컨트롤러가 모델을 변경할 때 `notifyAll` 메소드를 통해 변경 상태를 알릴 수 있게 된다. 그리고 이는 `update`메소드와 함께 `observers` 전체를 호출하게 된다.

```
function Model(){
  var self = this;
  this.heading = "Hello";
  //collection of observers
    this.observers = [];
  //add to the collection of observers
  this.registerObserver = function(observer){
    self.observers.push(observer);
  }
  //Iterate over observers, calling their update method
  this.notifyAll = function(){
    self.observers.forEach(function(observer){
      observer.update(self);
    })
  }
}
```

```
function View(controller){
    this.controller = controller;
    this.heading = document.getElementById(‘heading’);
    this.heading.addEventListener('click', controller);
    this.update = function(data){
         this.heading.innerText = data.heading;
    }
    this.controller.model.registerObserver(this);
}
```

```
function Controller(model){
    var self = this;
    this.model = model;
  //EVENTLISTENER INTERFACE
    this.handleEvent = function(e){
      e.stopPropagation();
      switch(e.type){
        case "click":
          self.clickHandler(e.target);
          break;
        default:
          console.log(e.target);
      }
    }
  //GET MODEL HEADING
    this.getModelHeading = function(){
      return self.model.heading;
    }
  //CHANGE THE MODEL
    this.clickHandler = function(target){
      self.model.heading = 'World';
     //now we just notify our observers
      self.model.notifyAll();
    }
}
```

```
참조:
https://medium.com/@patrickackerman/the-observer-pattern-with-vanilla-javascript-8f85ea05eaa8
https://www.hanbit.co.kr/media/channel/view.html?cms_code=CMS2276009419&cate_cd=
https://dev-momo.tistory.com/entry/State-Pattern-%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%8A%B8-%ED%8C%A8%ED%84%B4
```
