---
layout: post
title: "[java] 자바 안드로이드 앱 개발(Java Android app development)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

안드로이드 앱 개발은 현재 가장 인기 있는 분야 중 하나입니다. 안드로이드 앱을 개발하기 위해 주로 사용되는 언어 중 하나가 자바입니다. 이 글에서는 자바를 사용하여 안드로이드 앱을 개발하는 방법에 대해 알아보겠습니다.

## 개발 환경 설정

안드로이드 앱 개발을 위해 우선적으로 개발 환경을 설정해야 합니다. 다음 단계를 따라 진행해보세요.

1. JDK 설치: 자바 개발을 위해 JDK(Java Development Kit)를 설치해야 합니다. 공식적으로 Oracle에서 제공하는 JDK를 다운로드하여 설치합니다.

2. Android Studio 설치: 안드로이드 앱 개발을 위해 [Android Studio](https://developer.android.com/studio)를 다운로드하여 설치합니다. Android Studio는 자바용 안드로이드 개발 도구입니다.

3. 프로젝트 생성: Android Studio를 실행하고 새로운 안드로이드 프로젝트를 생성합니다. 프로젝트 설정이 완료되면 개발을 시작할 준비가 됩니다.

## 자바 코드 작성

안드로이드 앱에서 자바 코드를 작성하기 위해서는 주로 **액티비티(Activity)** 클래스를 사용합니다. 액티비티 클래스는 앱의 화면을 관리하고 액션에 응답하는 역할을 합니다.

다음은 간단한 안드로이드 앱을 만들기 위한 자바 코드의 예시입니다.

```java
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView greetingTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 레이아웃 파일에서 TextView 요소를 찾아 변수에 할당
        greetingTextView = findViewById(R.id.greeting_text);

        // TextView에 인사말 설정
        greetingTextView.setText("안녕하세요!");
    }
}
```

위 코드는 `MainActivity`라는 이름의 액티비티 클래스를 정의하고, `onCreate` 메소드에서 앱이 실행될 때 실행되는 코드를 작성합니다. `greetingTextView` 변수를 사용하여 화면에 "안녕하세요!"라는 텍스트를 표시합니다.

## 앱 실행 및 테스트

앱을 실행하고 테스트하기 위해 AVD(Android Virtual Device)를 설정해야 합니다. AVD는 가상으로 휴대폰 환경을 만들어 앱을 테스트하는 도구입니다.

Android Studio에서 AVD Manager를 이용하여 AVD를 설정합니다. AVD Manager에서 새 AVD를 생성하고 원하는 디바이스 버전과 스크린 사이즈 등을 선택합니다.

AVD 설정이 완료되면 Android Studio에서 앱을 실행하고 AVD에서 앱이 제대로 작동하는지 확인할 수 있습니다.

## 결론

이렇게 자바를 사용하여 안드로이드 앱을 개발할 수 있습니다. 안드로이드 앱 개발에는 자바 뿐만 아니라 다른 언어와 프레임워크도 사용할 수 있지만, 자바는 여전히 가장 널리 사용되는 언어 중 하나입니다.

더 자세한 안드로이드 앱 개발 방법과 자바 기술을 익히기 위해 [공식 안드로이드 개발자 문서](https://developer.android.com/docs)를 참조하시기 바랍니다.