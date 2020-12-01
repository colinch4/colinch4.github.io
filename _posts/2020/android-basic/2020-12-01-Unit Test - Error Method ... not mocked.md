---
layout: post
title: "[안드로이드 기초]  Unit Test - Error: Method ... not mocked"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


- 테스트 코드에 Json에 관련된 무언가가 있으면 에러가 발생하며 [링크](http://tools.android.com/tech-docs/unit-testing-support#TOC-Method-...-not-mocked.-)를 하나 던져준다. 그리고 링크에서는 아래와 같은 코드를 추가해주라고 한다. 왜일까?

> java.lang.RuntimeException: Method put in org.json.JSONObject not mocked. See [http://g.co/androidstudio/not-mocked](http://g.co/androidstudio/not-mocked) for details.

```groovy
testOptions {
    unitTests.returnDefaultValues = true
}
```

> If you run a test that calls an API from the Android SDK that you do not mock, you'll receive an error that says this method is not mocked. That's because the android.jar file used to run unit tests does not contain any actual code (those APIs are provided only by the Android system image on a device).
Instead, all methods throw exceptions by default. This is to make sure your unit tests only test your code and don't depend on any particular behavior of the Android platform (that you have not explicitly mocked, such as with Mockito).
If the exceptions thrown are problematic for your tests, you can change the behavior so that methods instead return either null or zero by adding the following configuration in your project's top-level build.gradle file:

안드로이드 공식 홈페이지에 따르면 이유는 이렇다.

- android.jar 파일이 유닛테스트 하는 곳에 사용되는데 해당 파일이 실제 코드를 가지고 있지는 않다.
- 그래서 포함되지 않은 method나 객체가 있으면 기본적으로 exception을 던진다.
- 이렇게 해놓은건 당신이 만들어놓은 테스트 코드만 돌리기 위해서, 그리고 Mockito 같은 걸로 명시적인 Mocking 빼고 안드로이드 플랫폼에 종속하지 않기 위해서이다. (대충 속도 때문에 막아놨다고 봐도 될듯하다.)
- 이러한 구성이 테스트 하는데 문제가 된다면, gradle에 세팅해서 메서드들이 null 또는 0을 반환하게 할 수 있다.

막상 위의 세팅을 그대로 따라하면 문제는 해결된다. 근데 주의할 점이 있더라.

> Caution: Setting the returnDefaultValues property to true should be done with care. The null/zero return values can introduce regressions in your tests, which are hard to debug and might allow failing tests to pass. Only use it as a last resort.

null 또는 0을 반환하게 하는 방법은 regression을 발생시킬 수 있다. Regression은 디버깅을 어렵게하고 실패한 테스트를 성공시킬지도 모른다. 그래서 이 방법은 최후의 수단으로 쓸 것.

Regression이 뭔데? 내가 아는 Regression은 한 곳에서 실패한게 다른 곳에도 영향을 미치는 건데? 아하. 해당 세팅을 사용하면 어떤 메서드가 null 또는 0을 반환시켜서 실패한 테스트도 성공시켜 버리니 어디서 실패했는지를 모르게 할 수 있다는 건가? 그렇다면 최후의 수단으로 사용하는게 맞겠네. 라는 추측을 내려보게 되었다.  
  
참고로 안드로이드 스튜디오가 소개해주는 해당 링크에는 경고문 하나 존재하지 않으니 주의하길 바란다. 역시 모든 정보는 [안드로이드 공식 홈페이지](https://developer.android.com/training/testing/unit-testing/local-unit-tests.html#error-not-mocked)를 참고...
