---
layout: post
title: "[디자인패턴] Abstract Factory 패턴"
description: " "
date: 2021-06-28
tags: [디자인패턴]
comments: true
share: true
---

# Abstract Factory 패턴

구체적인 클래스에 의존하지 않고 서로 연관되거나 의존적인 객체들의 조합을 만드는 인터페이스를 제공하는 패턴.

싱글턴, 팩토리 메서드 패턴을 사용한다.

추상 팩토리 패턴은 팩토리 메서드 패턴을 좀 더 캡슐화한 방식이라고 볼 수 있다.

서로 관련이 있는 객체들을 통째로 묶어서 팩토리 클래스를 만들고, 이들 팩토리를 조건에 따라 생성하도록 다시 팩토리를 만들어서 객체를 생성하는 패턴

관련성 있는 여러 종류의 객체를 일관된 방식으로 생성하는 경우에 유용하다.

\*\* 여기서 중요한건 TV와 TVFactory 함수(인터페이스)가 인터페이스의 역할을 함으로써 여러 팩토리가 같은 추상화된 같은 인터페이스를 통해서 관리가 가능하다는 것.

즉 밑의 코드는 TvProduct라는 클래스가 여러 상품 팩토리 객체를 통해 만들어진 상품 객체를 이용할 수 있는 코드이다.

    function Interface() {
      this.implements = function(obj) {
        var notImplementMethod = [];
        for(var method in this) {
          if(method !== "implements") {
            if(!Object.hasOwnProperty.call(obj.__proto__.method)){
              notImplementsMethod.push(method);
            }
          }
        }

        if(notImplementMethod.length > 0) {
          throw new Error(obj.__proto__.constructor.name + "클래스의" + notImplementMethod.join() + "메서드가 구현되지 않았습니다.")
        }
      }
    }

    //TV 인터페이스 선언

    function TV() {
      if(this.constructor === TV) {
        throw new Error(this.constructor.name + "인터페이스는 객체를 생성할 수 없습니다.")
      }
      return (function(){
        // 인터페이스 정의 메소드
        var method = {
          turnOn: function(){},
          turnOff: function(){},
          volumeUp: function(){},
          volumeDown: function(){},
        };
        interface.call(method);
        return method;
      })();
    };

    // TV 인터페이스를 구현하여 Samsung TV 클래스 선언

    function SamsungTV(model, price) {

      TV().implements(this);

      this.brand = "Samsung";

      this.model = model;

      this.price = price;

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


    // TV 인터페이스를 구현하여 LG TV 클래스 선언

    function LgTV(model, price) {

      TV().implements(this);

      this.brand = "LG";

      this.model = model;

      this.price = price;

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

    // TVFactory 인터페이스 선언

    function TVFactory(){

      if (this.constructor === TVFactory){

        throw new Error(this.constructor.name

          + ' 인터페이스는 객체를 생성할 수 없습니다.');

      }

      return (function(){

      // 인터페이스 정의 메서드

      var method = {

        create : function(){},

        setInfo : function(model, price){},

      };

      // 인터페이스의 implements 메서드를 method객체에 이식한다.

      Interface.call(method);

      return method;

    })();

};

    // TVFactory 인터페이스를 구현하여 SamsungTVFactory 클래스 선언

    function SamsungTVFactory(model, price) {

      this.model = model;

      this.price = price;

      TVFactory().implements(this);

    }

    SamsungTVFactory.prototype.create = function() {

      return new SamsungTV(this.model, this.price);

    };

    SamsungTVFactory.prototype.setInfo = function(model, price) {

      this.model = model;

      this.price = price;

      return this;

    };

    ​

    // TVFactory 인터페이스를 구현하여 SamsungTVFactory 클래스 선언

    function LgTVFactory(model, price) {

      this.model = model;

      this.price = price;

      TVFactory().implements(this);

    }

    LgTVFactory.prototype.create = function() {

      return new LgTV(this.model, this.price);

    };

    LgTVFactory.prototype.setInfo = function(model, price) {

      this.model = model;

      this.price = price;

      return this;

    };

    ​

    // 클라이언트 클래스

    var TVProduct = (function(){

      function TVProduct() {}

      TVProduct.prototype.getTV = function(tvFactory) {

        return tvFactory.create();

      }

      return new TVProduct();

    })();

    ​

    function test() {

      var samsungTVFactory = new SamsungTVFactory();

      var lgTVFactory = new LgTVFactory();

      var samsungTv = TVProduct.getTV(samsungTVFactory.setInfo("S-001", "1000000"));

      var samsungTv2 = TVProduct.getTV(samsungTVFactory.setInfo("S-002", "1000001"));

      var lgTv = TVProduct.getTV(lgTVFactory.setInfo("L-001", "1000001"));

      var lgTv2 = TVProduct.getTV(lgTVFactory.setInfo("L-002", "1000002"));

      samsungTv.turnOn(); // [Samsung(S-001) TV] turn on

      samsungTv2.turnOn(); // [Samsung(S-002) TV] turn on

      lgTv.turnOn(); // [LG(L-001) TV] turn on

      lgTv2.turnOn(); // [LG(L-002) TV] turn on

    }

    ​

    test();


    참조:
    https://blog.naver.com/PostView.nhn?blogId=mycho&logNo=221843113038&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postList
    https://victorydntmd.tistory.com/300
    https://gmlwjd9405.github.io/2018/08/08/abstract-factory-pattern.html
    https://gmlwjd9405.github.io/2018/08/08/abstract-factory-pattern.html
