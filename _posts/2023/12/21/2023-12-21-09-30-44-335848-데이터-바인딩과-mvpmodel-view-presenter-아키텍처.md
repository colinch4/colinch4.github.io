---
layout: post
title: "[android] 데이터 바인딩과 MVP(Model-View-Presenter) 아키텍처"
description: " "
date: 2023-12-21
tags: [android]
comments: true
share: true
---

## 데이터 바인딩이란 무엇인가?

데이터 바인딩은 안드로이드 개발에서 UI 컴포넌트와 백엔드 데이터 소스를 연결하여 일관성 있는 사용자 인터페이스를 제공하는 기술입니다. 안드로이드 스튜디오에서 데이터 바인딩을 활용하면 UI 구성 요소와 앱의 데이터 소스 간의 결속력을 강화하고 개발 생산성을 향상시킬 수 있습니다.

## MVP(Model-View-Presenter) 아키텍처란?

MVP 아키텍처는 안드로이드 앱을 설계하고 구현하는 데 사용되는 아키텍처 패턴입니다. MVP는 Model, View, Presenter의 약자로, 각각 데이터 처리, 화면 표시, 비즈니스 로직 분리를 담당합니다. 이를 통해 코드의 유지보수성과 확장성을 향상시킬 수 있습니다.

## 데이터 바인딩과 MVP 아키텍처의 결합

데이터 바인딩과 MVP 아키텍처를 함께 사용하면 안드로이드 앱을 보다 효율적으로 개발할 수 있습니다. MVP 아키텍처를 통해 화면 표시와 비즈니스 로직을 분리하고, 데이터 바인딩을 사용하여 UI 컴포넌트를 데이터와 결합시킴으로써 코드를 더욱 모듈화하고 유연하게 만들 수 있습니다.

아래는 데이터 바인딩과 MVP 아키텍처를 활용한 안드로이드 앱의 간단한 예시 코드입니다:

```java
public class MainActivity extends AppCompatActivity implements MainContract.View {
    private MainPresenter presenter;
    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);
        presenter = new MainPresenter(this);
        binding.button.setOnClickListener(view -> presenter.onButtonClick());
    }

    @Override
    public void displayData(String data) {
        binding.textView.setText(data);
    }
}

public interface MainContract {
    interface View {
        void displayData(String data);
    }

    interface Presenter {
        void onButtonClick();
    }
}

public class MainPresenter implements MainContract.Presenter {
    private MainContract.View view;

    public MainPresenter(MainContract.View view) {
        this.view = view;
    }

    @Override
    public void onButtonClick() {
        // 비즈니스 로직 처리
        String data = fetchData();
        view.displayData(data);
    }

    private String fetchData() {
        // 데이터 가져오는 로직
        return "Sample data";
    }
}
```

위의 예시 코드에서는 MVP 아키텍처를 활용하여 Presenter가 화면 표시 로직과 데이터 처리 로직을 분리하고, 데이터 바인딩을 사용하여 UI 컴포넌트와 데이터를 간편하게 연결하고 있습니다.

이처럼 데이터 바인딩과 MVP 아키텍처는 안드로이드 앱의 개발을 보다 효율적으로 만들고, 유지보수성과 확장성을 향상시키는 데 매우 유용하게 활용될 수 있습니다.

자세한 내용은 아래 참고자료를 참고해 주십시오.

## 참고 자료
- [Android Developers - Data Binding](https://developer.android.com/topic/libraries/data-binding)
- [Mindorks - MVP Architecture in Android using Kotlin](https://blog.mindorks.com/mvp-architecture-in-android-using-kotlin)