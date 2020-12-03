---
layout: post
title: "[RxAndroid] RxAndroid Basic: Part3"
description: " "
date: 2020-12-03
tags: [RxAndroid]
comments: true
share: true
---


Part1, 2는 몇 가지 예제를 따라가면서 RxJava의 주요 컨셉과 요소들에 대해 알아봄

Part3에서는 추가로 유용한 Observable과 Operator들에 대해 소개함



## 클릭의 추상화

안드로이드 위젯들을 위한 Observable이 구현되어 있는 RxBinding을 사용하면, 클릭 이벤트를 Observable 형태로 처리가 가능함

[RxBinding](https://github.com/JakeWharton/RxBinding)

- RxJava binding APIs for Android's UI widgets



```
compile 'com.jakewharton.rxbinding:rxbinding:0.3.0'
```

이 중 RxView.clicks이 가장 유용함

**RxView.clicks**

- View 타입을 인자로 받는 정적 메서드
- OnClickListener에 전달된 이벤트를 Observable 형태로 wrapping함

대부분의 안드로이드 위젯들이 View 타입을 상속하기 때문에 이 정적 메서드를 사용하면 간단하게 클릭 이벤트를 처리할 수 있음



```java
RxView
    .clicks(findViewById(R.id.button))
    .map(new Func1<Void, Integer>() {
      @Override
      public Integer call(Void event) {
        return new Random().nextInt();
      }
    })
    .subscribe(new Action1<Integer>() {
      @Override
      public void call(Integer value) {
		TextView.setText(value.toString())
      }
    });
```



## Merge



![Observable Merger](https://realm.io/assets/img/news/lk-rx3-merge.png)

여러 경로로 온 이벤트를 한 곳에서 처리해야할 때 개별 이벤트를 Observable로 받은 후 Merge해서 처리할 수 있음

```java
Observable<String> lefts = RxView
    .clicks(findViewById(R.id.button_left))
    .map(new Func1<Void, String>() {
        @Override
        public String call(Void aVoid) {
            return "left click";
        }
    });

Observable<String> rights = RxView
    .clicks(findViewById(R.id.button_right))
    .map(new Func1<Void, String>() {
        @Override
        public String call(Void aVoid) {
            return "right click";
        }
    });

Observable<String> together = Observable.merge(lefts, rights);
together
    .map(new Func1<String, String>() {
        @Override
        public String call(String s) {
            return s.toUpperCase();
        }
    })
    .subscribe(new Action1<String>() {
    @Override
    public void call(String s) {
        ((TextView) findViewById(R.id.text_view)).setText(s);
    }
});

```





## Combine - 여러 이벤트를 한 번에

여러 조건에 따라 처리해야 하는 이벤트

예를 들면,

- 체크 박스가 체크되고, 텍스트 에디터가 채워졌을 때만 버튼을 활성화 해야 할 경우

```java
checkBox1 = (CheckBox) findViewById(R.id.check_box);
password1 = (EditText) findViewById(R.id.edit_text_password);

Observable<Boolean> check1 = RxCompoundButton.checkedChanges(checkBox1);

Observable<Boolean> textExist1 = RxTextView.textChanges(password1)
    .map(new Func1<CharSequence, Boolean>() {
        @Override
        public Boolean call(CharSequence charSequence) {
            return charSequence.length() != 0;
        }
    });

Observable<Boolean> textValidation1 = Observable.combineLatest(check1, textExist1, new Func2<Boolean, Boolean, Boolean>() {
    @Override
    public Boolean call(Boolean check, Boolean exist) {
        password1.setEnabled(check);
        Log.d(TAG, "check=" + check + ", exist=" + exist);
        return exist;
    }
});

final Button submit = (Button) findViewById(R.id.button_submit);

textValidation1.subscribe(new Action1<Boolean>() {

    @Override
    public void call(Boolean enable) {
        submit.setEnabled(enable);
    }
});

```

1.  RxCompoundButton.checkedChanges를 이용해서 체크박스 이벤트를 처리할 수 있는 Observable 생성
2. xTextView.textChanges를 이용해서 텍스트에디터의 텍스트 변경 여부를 확인할 수 있는 Observable 생성
3. map으로 텍스트 길이를 확인하여 텍스트에디터가 비었는지를 확인하는 Observable 생성
4. combinLatest에 두 가지 Observables을 넣어서 둘 중 하나라도 변경되면 두 조건 값을 확인할 수 있는 Observable을 생성
5. combinLastest가 생성한  Observable을 구독해서 두 가지 조건이 모두 만족될 때 submit button이 활성화 되도록 함