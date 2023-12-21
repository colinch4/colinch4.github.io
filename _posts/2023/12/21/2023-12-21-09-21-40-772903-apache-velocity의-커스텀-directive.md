---
layout: post
title: "[java] Apache Velocity의 커스텀 Directive"
description: " "
date: 2023-12-21
tags: [java]
comments: true
share: true
---

Apache Velocity는 템플릿 언어를 사용하여 동적 콘텐츠를 생성하는 데 사용되는 강력한 템플릿 엔진입니다. Velocity는 사용자 정의 Directive를 통해 확장이 가능합니다.

## 커스텀 Directive란?

Velocity의 Directive는 Velocity 템플릿에서 사용할 수 있는 특별한 키워드이며, 사용자가 직접 정의할 수도 있습니다. 이러한 커스텀 Directive를 만들어서 Velocity 엔진에 추가하면 템플릿에서 사용자 정의한 동작을 수행할 수 있습니다.

## 커스텀 Directive 만들기

Velocity에서 커스텀 Directive를 만들려면 `org.apache.velocity.runtime.directive.Directive` 클래스를 확장해야 합니다. 이 클래스를 상속받아 `render()` 메서드를 구현하여 Directive의 동작을 정의할 수 있습니다.

다음은 간단한 예제 코드입니다.

```java
import org.apache.velocity.runtime.parser.node.Node;
import org.apache.velocity.context.InternalContextAdapter;
import org.apache.velocity.exception.ParseErrorException;
import org.apache.velocity.exception.ResourceNotFoundException;
import org.apache.velocity.exception.MethodInvocationException;

public class CustomDirective extends Directive {

    @Override
    public String getName() {
        return "myCustomDirective";
    }

    @Override
    public int getType() {
        return LINE;
    }

    @Override
    public boolean render(InternalContextAdapter context, Writer writer, Node node) 
        throws IOException, ResourceNotFoundException, ParseErrorException, MethodInvocationException {
        // 커스텀 Directive의 동작을 구현
        // 입력 파라미터를 처리하고 출력을 생성
        return true;
    }
}
```

## 커스텀 Directive 등록

만든 커스텀 Directive를 Velocity 엔진에 등록해야 합니다. 이를 위해 `VelocityEngine`의 `addDirective()` 메서드를 사용하여 커스텀 Directive를 등록합니다.

```java
VelocityEngine velocityEngine = new VelocityEngine();
velocityEngine.init();

velocityEngine.addDirective("myCustomDirective", new CustomDirective());
```

위 예제에서 `myCustomDirective`는 템플릿에서 사용할 수 있는 Directive의 이름입니다.

## 커스텀 Directive 활용

이제 템플릿에서 만든 커스텀 Directive를 사용할 수 있습니다. 

```
#parse("header.vm")
Welcome to our site, $username! 
#myCustomDirective(parameter)
#parse("footer.vm")
```

위 예제에서 `#myCustomDirective(parameter)`는 사용자가 만든 커스텀 Directive를 호출하는 부분입니다.

커스텀 Directive를 만들고 활용함으로써 Velocity 템플릿 언어의 기능을 확장할 수 있습니다.

기타 자세한 내용은 [Apache Velocity 공식 문서](https://velocity.apache.org/engine/2.3/apidocs/)를 참조하세요.