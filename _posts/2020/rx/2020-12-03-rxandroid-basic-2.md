---
layout: post
title: "[RxAndroid] RxAndroid Basic: Part2"
description: " "
date: 2020-12-03
tags: [android]
comments: true
share: true
---


[RxAndroid Basic: Part2](https://medium.com/@kurtisnusbaum/rxandroid-basics-part-2-6e877af352#.7cepyfaz1)



Part1에서는 

- RxJava의 가장 핵심적인 두 가지 요소 Observable과 Observer에 대해 이해
- 비동기로 데이터 로드
- Observable과  Observer의 실행 Thread 지정

에 대해서 알아봤습니다. 

이제 좀 더 응용 버전의 Observable과 Operators 예제들을 살표보도록 하겠습니다. 



## Example 4: Subjects

예제 설명

- 숫자를 증가시키기 위한 버튼을 가진 Activity를 만들어보자



예제 보기 전에 또 하나의 RxJava Concept : Subject

**Subject**

- **Both** an Observable and an Observer
- as a pipe
- Subject의 한 쪽 끝으로 입력을 넣으면 반대쪽으로 나옴

> Subject은 Event를 전달 받아 Observer들에게 Event를 전파하는 중간 다리로 볼 수 있습니다. 
>
> Android에서는 EventBus와 같은 형태로 사용이 가능합니다. 



Subject은 여러 타입이 있는데 여기서는 그 중에서 가장 간단한 PublishSubject를 사용함

With PublishSubject

- 한 쪽 끝으로 입력을 넣으면 그 즉시 반대쪽으로 나옴

이제 그 반대쪽으로 나오는 결과를 후킹을 하려고 함

Subject은 Observable이기 때문에 Observe할 수 있음. 

이를 이용해서 pip의 반대쪽 끝에서 나오는 결과를 지켜보는 것이 가능함



```java
mCounterEmitter = PublishSubject.create();
mCounterEmitter.subscribe(new Observer<Integer>() {
  
  @Override
  public void onCompleted() {}
  
  @Override
  public void onError(Throwable e) {}
  
  @Override
  public void onNext(Integer integer) {
    mCounterDisplay.setText(String.valueOf(integer));
  }
});
```



PublishSubject는 value를 어떻게 발행하나?

```java
mIncrementButton.setOnClickListener(new View.OnClickListener() {

    @Override 
    public void onClick(View v) { 
        mCounter++;
        mCounterEmitter.onNext(mCounter);
    }
});
```

mIncrementButton 두 가지 일을 함

1. mCounter 값을 증가시킴
2. mCounterEmitter(PublishSubject)의 onNext() 메서드를 호출함

Subjects은 Observer이기도 하기 때문에 onNext() 메서드를 가짐

즉, 위의 예제들은 아래와 같은 흐름으로 실행됨

1. Subject의 onNext() 메서드를 호출해 pipe의 한 쪽 끝으로 mCounter를 집어 넣음
2. Subject은 onNext() 메서드를 통해 들어온 mCounter를 value로 발행함
3. Subject을 subscribe하고 있던 Observer는 value로 발행된 mCounter를 onNext 콜백으로 받음



이런 특징을 이용하면 EventBus처럼 Activity나 앱의 Lifecycle과 동일하게 살아있도록 해서 Event를 전파하는 역할로 사용할 수 있음



## Example 5: Map()

예제 설명

- 단순히 숫자를 화면에 보여주는 Activity



새로운 RxJava Concept: map

**map**

- Functional Programming에서 주로 값을 변형하는 함수로 많이 쓰임
- 하나의 데이터를 다른 데이터로 바꾸는 operator(참고, [RxJava의 다양한 operators](http://reactivex.io/documentation/operators.html))
- 원본 스트림(Observable)을 변경하지 않고, 변형된 새로운 스트림(Observable)을 생성함


![데이터 가공 Map](https://realm.io/assets/img/news/lk-rx2-1.png)

**Operator**

- Observable이 발행하는 데이터들을 변환, 결합, 조작하는 기능을 제공하고, 그 결과를 새로운 Observable로 반환함
- 연속된 비동기 호출을 구성할 수 있음 
- **중첩된 콜백 핸들러**로 인한 콜백 지옥에서 해방



Value 4를 발행하는 Single 예제

```java
Single.just(4).map(new Func1<Integer, String>() { 
    
    @Override 
    public String call(Integer integer) { 
        return String.valueOf(integer);
    } 
}).subscribe(new SingleSubscriber<String>() { 
    
    @Override 
    public void onSuccess(String value) { 
        mValueDisplay.setText(value); 
    } 
    
    @Override 
    public void onError(Throwable error) { } 
});
```

숫자 4가 발행되지만 text로 표시해야 되기 때문에 map을 이용해서 Interger 4를 String로 변환해서 전달함

**Observable에서 발행한 데이터를 받아서 변환 또는 추가 로직을 수행해서 다시 Observable로 반환**





## Example 6: Bringing it All Together

예제 설명

- 사용자가 이름으로 도시를 찾을 수 있도록 도와주는 Activity

지금까지 배운거 다 동원한  mega-example



New RxJava Concept: debounce

**debounce**

- 일정 시간 이상 으로 입력이 들어오지 않을 때만 데이터를 발행하라고 Subject에게 알림



자, 시작해봅시다. 

```java
mTextWatchSubscription = mSearchResultsSubject
  .debounce(400, TimeUnit.MILLISECONDS)
  .observeOn(Schedulers.io())
  .map(new Func1<String, List<String>() {
    
    @Override
    public List<String> call(String s) {
      return mRestClient.searchForCity(s);
    }
  })
  .observeOn(AndroidSchedulers.mainThread())
  .subscribe(new Observer<List<String>>() {
    
    @Override
    public void onCompleted() {}
    
    @Override
    public void onError(Throwable e) {}
    
    @Override
    public void onNext(List<String> cities) {
      handleSearchResults(cities);
    }
  });

mSearchInput.addTextChangedListener(new TextWatcher() {
  
  @Override
  public void beforeTextChanged(CharSequence s, int start, int count, int after) {}
  
  @Override
  public void onTextChanged(CharSequence s, int start, int before, int count) {
    mSearchResultsSubject.onNext(s.toString())
  }
  
  @Override
  public void afterTextChanged(Editable s) {}
});
```



위의 예제에서 TextWatcher는 사용자가 키보드를 입력할 때마다 onTextChanged 발생하고, mSearchResultsSubject의 onNext가 불려서 사용자가 입력한 값이 발행되도록 되어 있음. 하지만, 사용자가 키보드를 입력할 때마다 value를 발행해서 해당 value로 서버에 요청을 보내는 것은 바람직하지도 않고, 원하는 바도 아님.

**즉, 우리가 원하는 것은 일정 시간 이상 사용자가 입력이 없을 때만 사용자가 지금까지 입력한 값으로 서버에 요청하는 것임**

이를 가능하게 하는 것이 debounce()임

위의 예제에서는 400ms동안 사용자의 입력이 없으면, 입력 값으로 서버에 요청함



.observeOn(Schedulers.io())

- mSearchResultsSubject이 발행한 값을 io scheduler에서 받을 수 있도록 함

.map

- 발행된 값을 가지고 비동기로 서버에 요청하고, 결과가 오면 Observable을 반환함

.observeOn(AndroidSchedulers.mainThread())

- map이 반환한 Observable이 발행하는 값을 받는 Observer가 UI Thread에서 실행되도록 함

.subscribe

- map으로 부터 반환된 Observable로부터 발행된 값을 받아서 UI 처리함



```
mSearchResultsSubject 
         |
         |
         V
      debounce
        ||| 
        |||
         V 
        map 
         | 
         | 
         V
      observer
```

- | - UI Thread에서 발행되는 것을 표현
- ||| - IO Scheduler에서 발행되는 것을 표현




## 마치며

RxJava의 가장 기본적인 concept과 몇 개의 예제를 살펴봤음

RxJava에는 이밖에도 아주 많은 Operator들이 있기 때문에 다양한 응용을 위해서는 추가로 살펴볼 것을 추천함



아직 RxJava의 기본 컨셉을 이해한 수준이지만, 이번 Part1에서 언급한 장점만으로도 충분히 안드로이드 앱 개발자에게 매력적으로 느껴질 수 있는 라이브리러가 아닌가 하는 생각이 듭니다. 

