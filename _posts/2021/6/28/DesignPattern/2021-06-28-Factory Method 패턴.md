---
layout: post
title: "[디자인패턴] Factory Method 패턴"
description: " "
date: 2021-06-28
tags: [디자인패턴]
comments: true
share: true
---

## Factory Method 패턴

객체를 만들어내는 부분을 서브 클래스에 위임하는 패턴

즉 객체를 만들어내는 공장을 만드는 패턴이라고 이해하면 쉽다.

어떤 상황과 조건에 따라 객체를 다르게 생성해야 할 때가 있다. 사용자의 입력값에 따라 하는 일이 달라질 경우, 분기를 통해 특정 객체를 생성해야한다.

하지만 아래와 같은 경우를 보자.

```
class Type {

}

class TypeA extends Type {

    TypeA() {
        console.log("Type A 생성");
    }

}

class TypeB extends Type {

    TypeB() {
        console.log("Type B 생성");
    }

}

class TypeC extends Type {

    TypeC() {
        console.log("Type C 생성");
    }

}

class ClassA {
  createType(str) {
        let returnType = null;

        switch (str){
            case "A":
                returnType = new TypeA();
                break;

            case "B":
                returnType = new TypeB();
                break;

            case "C":
                returnType = new TypeC();
                break;
        }

        return returnType;
  }

}

class Client {

    constructor(...args){
        const classA = new ClassA();

        console.log(classA.createType("A"));
        console.log(classA.createType("C"));
    }

}

```

위는 Type과 TypeA,B,C 클래스를 정의하고 캡슐화 한 코드이다. ClassA의 createType() 메서드에서 문자열에 따라 Type클래스 생성을 분기처리 하고 있다. 하지만 아래와 같이 여러 클래스에서 위의 분기처리하여 객체를 생성하는 코드를 쓰는 경우라면 중복된 코드가 발생한다.
또한 문자열에 따라 분기하기 때문에 Class와 Type 간의 결합도가 높아지게 된다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile21.uf.tistory.com%2Fimage%2F99B53E475C2593AB2B4DE1">

위와 같이 객체를 생성하는 부분은 사용하는 클래스에서 하지않고 팩토리 클래스를 만들어 사용하는 방식을 팩토리 메서드 패턴이라고 한다.

위의 코드에서 두가지 사항의 변경이 필요하다.

1. 팩토리 클래스를 정의
2. 객체 생성을 필요로 하는 클래스(Class A)에서 팩토리 클래스의 객체를 생성하여 분기에 따른 객체 생성 메서드를 호출

```

class TypeFactory {
  createType(str) {
        let returnType = null;

        switch (str){
            case "A":
                returnType = new TypeA();
                break;

            case "B":
                returnType = new TypeB();
                break;

            case "C":
                returnType = new TypeC();
                break;
        }

        return returnType;
  }
}

class ClassA {
  constructor(str) {
    const factory = new TypeFactory();

    const returnType = factory.createType(str)

    return returnType;
  }
}

```

패턴 적용 전에는 ClassA에서 하던 일을 TypeFactory에서 진행하고 있다.

즉 조건에 따른 객체 생성 부분을 자신이 직접하지 않고, 팩토리 클래스에 위임하여 객체를 생성하도록 하는 방법이 팩토리 메서드 패턴이다.

위의 방식은 객체 생성을 factory에서 하므로 사용하는 class와의 결합도를 낮춰서 사용할 수 있게 된다.

```
function Interface() {

  this.implements = function(obj) {

    // this는 인터페이스, obj는 인터페이스를 implements한 클래스

    var notImplementMethod = [];

    for(var method in this) {

      if(method !== 'implements') {

        // obj.__proto__ 객체가 method를 가지고 있지 않으면

        if(!Object.hasOwnProperty.call(obj.__proto__, method)) {

          notImplementMethod.push(method);

        }

      }

    }

    if(notImplementMethod.length > 0) {

      throw new Error(obj.__proto__.constructor.name + " 클래스의 "

      + notImplementMethod.join() + " 메서드가 구현되지 않았습니다.");

    }

  }

}

​

function Abstract() {

  this.implements = function(obj) {

    // this는 추상클래스, obj는 추상클래스를 상속한 클래스

    var notImplementMethod = [];

    for(var method in this) {

      if(method !== 'implements' && method !== 'copyMethod') {

        // obj.__proto__ 객체가 method를 가지고 있지 않으면

        if(typeof this[method] === "function"

          && this[method].abstract

          && !Object.hasOwnProperty.call(obj.__proto__, method)) {

          notImplementMethod.push(method);

        }

      }

    }

    if(notImplementMethod.length > 0) {

      throw new Error(obj.__proto__.constructor.name + " 클래스의 "

      + notImplementMethod.join() + " 메서드가 구현되지 않았습니다.");

    }

    return this;

  }

  this.copyMethod = function(fn, method, abstractMethod) {

    for(var m in method) {

      fn.prototype[m] = method[m];

    }

    for(var m in abstractMethod) {

      fn.prototype[m] = abstractMethod[m];

      fn.prototype[m].abstract = true;

    }

  }

  return this;

}

​

// TV 인터페이스 선언

function TV(){

  if (this.constructor === TV){

    throw new Error(this.constructor.name

      + ' 인터페이스는 객체를 생성할 수 없습니다.');

  }

  return (function(){

    // 인터페이스 정의 메서드

    var method = {

      turnOn : function(){},

      turnOff : function(){},

      volumeUp : function(){},

      volumeDown : function(){},

    };

    // 인터페이스의 implements 메서드를 method객체에 이식한다.

    Interface.call(method);

    return method;

  })();

};

​

// TV 인터페이스를 구현하여 Samsung TV 클래스 선언

function SamsungTV(model, speaker) {

  TV().implements(this);

  this.brand = "Samsung";

  this.model = model;

}

SamsungTV.prototype.turnOn = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] turn on");

};

SamsungTV.prototype.turnOff = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] turn off");

};

SamsungTV.prototype.volumeUp = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] volumn up");

};

SamsungTV.prototype.volumeDown = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] volumn Down");

};

​

// TV 인터페이스를 구현하여 Lg TV 클래스 선언

function LgTV(model, speaker) {

  TV().implements(this);

  this.brand = "LG";

  this.model = model;

}

LgTV.prototype.turnOn = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] turn on");

};

LgTV.prototype.turnOff = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] turn off");

};

LgTV.prototype.volumeUp = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] volumn up");

};

LgTV.prototype.volumeDown = function() {

  console.log("[" + this.brand + "(" + this.model + ") TV] volumn Down");

};

​

// TVCreator 추상클래스 정의

var TVCreator = (function(){

  var className = "TVCreator";

  function fn(brand){

    if (this.constructor === fn){

      throw new Error(className

        + ' 추상클래스는 객체를 생성할 수 없습니다.');

    }

​

    return this.implements(this);

  }



  // 인터페이스 정의 메서드

  var method = {

    testTV : function() {

      var tv = this.createTV();

      tv.turnOn();

      tv.volumeUp();

      tv.volumeDown();

      tv.turnOff();

    }

  };

  var abstractMethod = {

    createTV : function(){},

  };

  // 추상클래스의 extends 메서드를 method객체에 이식한다.

  Abstract.call(method).copyMethod(fn, method, abstractMethod);

  return fn;

})();

​

// TVCreator 클래스를 상속하여 SamsungTVCreator 클래스 정의

function SamsungTVCreator() {

  TVCreator.call(this);

}

SamsungTVCreator.prototype = Object.create(TVCreator.prototype);

SamsungTVCreator.prototype.constructor = SamsungTVCreator;

SamsungTVCreator.prototype.createTV = function() {

  return new SamsungTV("S-001");

}

// TVCreator 클래스를 상속하여 LgTVCreator 클래스 정의

function LgTVCreator() {

  TVCreator.call(this);

}

LgTVCreator.prototype = Object.create(TVCreator.prototype);

LgTVCreator.prototype.constructor = LgTVCreator;

LgTVCreator.prototype.createTV = function() {

  return new LgTV("L-001");

}

​

// 클라이언트

function Client() {};

Client.prototype.test = function() {

  var brand = "Samsung";

  // var brand = "LG";

  var tvCreator = null;

  if(brand === "Samsung") {

    tvCreator = new SamsungTVCreator();

  }

  else if(brand === "LG") {

    tvCreator = new LgTVCreator();

  }



  tvCreator.testTV();

 }

​

new Client().test();

// 출력

// [Samsung(S-001) TV] turn on

// [Samsung(S-001) TV] volumn up

// [Samsung(S-001) TV] volumn Down

// [Samsung(S-001) TV] turn off

​

// [LG(L-001) TV] turn on

// [LG(L-001) TV] volumn up

// [LG(L-001) TV] volumn Down

// [LG(L-001) TV] turn off
[출처] Javascript Factory Method 패턴|작성자 민경아빠
```

      참조:
      https://blog.naver.com/PostView.nhn?blogId=mycho&logNo=221845666149&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postList&userTopListOpen=true&userTopListCount=30&userTopListManageOpen=false&userTopListCurrentPage=1
      https://victorydntmd.tistory.com/299
      https://jdm.kr/blog/180
