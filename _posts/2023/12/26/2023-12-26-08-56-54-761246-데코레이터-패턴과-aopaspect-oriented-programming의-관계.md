---
layout: post
title: "[c#] 데코레이터 패턴과 AOP(Aspect-Oriented Programming)의 관계"
description: " "
date: 2023-12-26
tags: [c#]
comments: true
share: true
---

데코레이터 패턴과 AOP는 모두 객체 지향 프로그래밍에서 유용하게 활용되는 기법들입니다. 각각의 특징과 장단점을 살펴보면서 두 가지 기법 간의 관계를 살펴보겠습니다.

## 데코레이터 패턴 

데코레이터 패턴은 객체의 기능을 동적으로 확장하거나 변경할 수 있게 해주는 구조적인 패턴입니다. 

다음은 간단한 데코레이터 패턴의 예시입니다.

```csharp
public interface IComponent
{
    void Operation();
}

public class ConcreteComponent : IComponent
{
    public void Operation()
    {
        Console.WriteLine("Performing operation");
    }
}

public abstract class Decorator : IComponent
{
    private readonly IComponent _component;

    protected Decorator(IComponent component)
    {
        _component = component;
    }

    public virtual void Operation()
    {
        _component.Operation();
    }
}

public class ConcreteDecoratorA : Decorator
{
    public ConcreteDecoratorA(IComponent component) : base(component) { }

    public override void Operation()
    {
        base.Operation();
        Console.WriteLine("Modified by ConcreteDecoratorA");
    }
}

public class ConcreteDecoratorB : Decorator
{
    public ConcreteDecoratorB(IComponent component) : base(component) { }

    public override void Operation()
    {
        base.Operation();
        Console.WriteLine("Modified by ConcreteDecoratorB");
    }
}

// Usage
IComponent component = new ConcreteComponent();
component = new ConcreteDecoratorA(component);
component = new ConcreteDecoratorB(component);
component.Operation();
```

데코레이터 패턴을 사용하면 기존 객체의 동작을 유연하게 변경할 수 있습니다. 이는 실행 시간 동안 객체의 동작을 변경하는 방식으로, 개별 객체가 응집력 있게 유지됩니다.

## AOP(Aspect-Oriented Programming)

AOP는 관심사(Concern)에 초점을 맞춘 프로그래밍 기법으로, 횡단 관심사(cross-cutting concerns)와 핵심 관심사(core concerns)를 분리하여 모듈화하는 것을 목표로 합니다. 이를 통해 코드의 재사용성과 유지보수성을 향상시킬 수 있습니다.

데코레이터 패턴과 AOP는 모두 동적인 기능 추가 및 변경을 목표로 하지만, AOP는 주로 횡단 관심사에 대한 처리를 위해 사용되며, **데코레이터 패턴은 개별 객체의 동작을 확장 또는 변경하는 데 사용됩니다**.

## 결론

데코레이터 패턴과 AOP는 객체 지향 프로그래밍에서 유사한 목적을 가지고 있지만, 적용되는 분야와 목적에 있어서 차이를 가집니다. 데코레이터 패턴은 개별 객체의 동적인 확장 또는 변경을 위해 사용되며, AOP는 애플리케이션 전반적으로 횡단 관심사를 다루는 데 활용됩니다.

_[참고 자료](https://en.wikipedia.org/wiki/Decorator_pattern)_
_[참고 자료](https://en.wikipedia.org/wiki/Aspect-oriented_programming)_