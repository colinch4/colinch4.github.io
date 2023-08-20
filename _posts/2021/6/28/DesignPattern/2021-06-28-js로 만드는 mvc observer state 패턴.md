---
layout: post
title: "[디자인패턴] js로 만드는 mvc+observer+state 패턴"
description: " "
date: 2021-06-28
tags: [디자인패턴]
comments: true
share: true
---


## js로 만드는 mvc+observer+state 패턴

일련의 규칙에 따라 객체의 상태를 변화시켜 객체가 할 수 있는 행위를 바꾸는 패턴이다.

객체의 특정 상태를 클래스로 선언하고 해당 클래스에서 해당 상태에서 할 수 있는 행위들을 메서드로 정의한다.

<img src="https://miro.medium.com/max/800/1*2jtLuxLDN7J4PFgPByZAqQ.png">

상태를 조작할 수 있고, 해당 상태를 갖고 있는 객체의 참조를 통해 해당 상태를 사용할 수 있게 만드는 객체가 필요하다. 이를 위해서 현재 상태에 대한 참조를 저장하고, 이 상태를 변화 시킬 수 있는 메소드를 가진 코드를 작성해야 한다.

```
function HeadingState(){
  var self = this;
  this.state = new HelloState(self);
  this.changeState = function(){
    self.state.next();
  }
  this.getValue = function(){
    return self.state.value
  }
}
```

위 코드는 `HeadingState`의 인스턴스에 초기상태와, 상태 변화, 상태를 가져올 수 있게 설정한다. new HelloState의 인자로 HeadingState 객체를 전달함으로써 각 state class들은 인자로 `HeadingState` 싱글톤을 사용하게 된다.

```
function HelloState(container){
  var self = this;
  this.container = container;
  this.value = 'Hello';
  container.state = this;
  this.next = function(){
    return new WorldState(self.container);
  }
}
function WorldState(container){
  var self = this;
  this.container = container;
  this.value = 'World';
  container.state = this;
  this.next = function(){
    return new HelloState(self.container);
  }
}
```

위 코드에서 전달받은 container, 즉 HeadingState 싱글톤은 각 상태 객체로 전달 되어 각 상태 객체에서 전달 받아야 하는 행위가 포함된 값을 this(객체)로 전달 받는다. 현재는 상태가 두개 이므로 next란 메소드를 통해 새로운 상태 객체를 생성하는데 상태들이 많아지면 메소드 이름의 변경이 필요할 것으로 보이고 모델 내부의 로직도 변경되어야 한다.

```
function Model(){
  var self = this;
  var state = new HeadingState();
  var heading = state.getValue();
  this.observers = [];
  this.registerObserver = function(observer){
    self.observers.push(observer);
  }
  this.notifyAll = function(){
    self.observers.forEach(function(observer){
      observer.update(self);
    })
  }
  //add changeHeading method to toggle state;
  this.changeHeading = function(){
    console.log('change heading');
    state.changeState();
    self.heading = state.getValue();
  }
  Object.defineProperty(this,"heading",{
    get: function() { return heading; },
    set: function(value) {
      heading = value;
      this.notifyAll();
    }
  });
}
```

모델에서 state에 초기 HeadingState 생성자의 인스턴스를 할당 받아서 changeHeading이 호출 될 때 `HeadingState`의 싱글톤 인스턴스에서 해당하는 상태를 갖게 된다.

위 코드에서 heading은 var로 선언된 지역 변수이지만 `self.heading` 즉 this.heading에 할당한 이유는 밑의 defineProperty의 setter를 활용하기 위함이다.

state 패턴은 언뜻보면 귀찮을 수 있지만, 어플리케이션을 작성할 때 잠재적으로 아직은 추가되지 않은 상태들을 추후에 추가할 때 유용하다.
각 상태들은 상태에 따른 로직들을 캡슐화 하여 적용할 수 있기 때문에 switch case를 사용했을 때 유지보수적인 관점에서 훨씬 좋다.

참조:
https://medium.com/@patrickackerman/the-state-pattern-with-vanilla-javascript-e40ff83e85d0
