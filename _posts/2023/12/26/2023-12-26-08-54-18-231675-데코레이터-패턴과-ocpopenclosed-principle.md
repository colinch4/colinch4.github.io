---
layout: post
title: "[c#] 데코레이터 패턴과 OCP(Open/Closed Principle)"
description: " "
date: 2023-12-26
tags: [c#]
comments: true
share: true
---

데코레이터 패턴은 객체 지향 프로그래밍에서 유연한 디자인을 위해 사용되는 패턴 중 하나입니다. 이 패턴은 객체에 새로운 기능을 동적으로 추가할 수 있게 해주며, **OCP(Open/Closed Principle)**를 준수하는 방법 중 하나로 자주 사용됩니다.

## OCP(Open/Closed Principle)란?

OCP는 소프트웨어 설계 원칙 중 하나로, 소프트웨어 엔티티(클래스, 모듈, 함수 등)는 **확장에는 열려 있고 변경에는 닫혀** 있어야 한다는 원칙을 말합니다. 즉, 기존의 코드를 변경하지 않고 새로운 기능을 추가할 수 있어야 합니다.

## 데코레이터 패턴

데코레이터 패턴은 기존의 코드를 변경하지 않고 새로운 기능을 추가하는 방법을 제공합니다. 주로 상속을 통한 기능 추가가 한계가 있을 때 활용됩니다.

```c#
public interface IComponent 
{
    string Operation();
}

public class ConcreteComponent : IComponent 
{
    public string Operation() 
    {
        return "ConcreteComponent";
    }
}

public abstract class Decorator : IComponent 
{
    protected IComponent component;

    public Decorator(IComponent component) 
    {
        this.component = component;
    }

    public virtual string Operation() 
    {
        return component.Operation();
    }
}

public class ConcreteDecoratorA : Decorator 
{
    public ConcreteDecoratorA(IComponent component) : base(component) { }

    public override string Operation() 
    {
        return $"ConcreteDecoratorA({base.Operation()})";
    }
}

public class ConcreteDecoratorB : Decorator 
{
    public ConcreteDecoratorB(IComponent component) : base(component) { }

    public override string Operation() 
    {
        return "ConcreteDecoratorB";
    }
}
```

위 코드는 데코레이터 패턴을 사용하여 기존의 `ConcreteComponent`에 새로운 기능을 추가하는 간단한 예제입니다. 

## 마무리

데코레이터 패턴은 OCP를 준수하면서도 유연한 기능 확장이 가능하도록 도와줍니다. 이 패턴을 적절히 활용하여 코드의 확장성과 유지보수성을 향상시킬 수 있습니다.

참고 문헌: [메타포 디자인 패턴 - 데코레이터 패턴](https://jaeyeophan.github.io/2017/05/14/DecoratorPattern/)