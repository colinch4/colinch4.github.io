---
layout: post
title: "[dagger] Dagger2 Practice"
description: " "
date: 2020-12-03
tags: [dagger]
comments: true
share: true
---


Dagger2를 이용하고 적용해보기 위해 실제 프로젝트에서 모듈화하려던 일부 코드를 가져와서 진행한 practice 설명 페이지 입니다.

## 1. Dagger2 API (annotation)
Dependency Injection을 위해 정의한 자바 표준 annotation을 이용함

#### @Inject
Dependency Injection framework으로 부터 의존성이 주입되어야 함을 표시합니다.  
즉, 의존성 주입을 요청하는 역할을 한다고 보면 됩니다.   
Constructor, Field, Method를 이용한 세 가지 방법이 있습니다.
```
@Inject
public WifiBasedHomeComingAware(Context context, @WifiNetwork WifiStateReceiver wifiStateReceiver) {
    this.context = context;
    this.wifiStateReceiver = wifiStateReceiver;
}
```

```
@Inject @Wifi
HomeComingAware homeComingAware;
```


#### @Module + @Provides
실제 의존성을 제공하는 역할을 합니다. @Module을 클래스에 표시하고, @Provides는 각각의 메서드에 표시합니다.

```
@Module
public class HomeComingAwareModule {
    private final static String TAG = HomeComingAwareModule.class.getSimpleName();
    private final Context context;

    public HomeComingAwareModule(Context context) {
        this.context = context;
    }

    @Provides
    Context provideContext() {
        return this.context;
    }

    @Provides @Wifi
    HomeComingAware provideWifiBasedHomeComingAware(WifiBasedHomeComingAware wifiBasedHomeComingAware) {
        return wifiBasedHomeComingAware;
    }

    @Provides @Location
    HomeComingAware provideLocationBasedHomeComingAware(LocationBasedHomeComingAware locationBasedHomeComingAware) {
        return locationBasedHomeComingAware;
    }
}
```

#### @Component
의존성을 요청하는 @Inject와 의존성을 제공하는 @Module + @Provides 사이의 연결고리 역할을 합니다.
```
@Singleton
@Component(dependencies = {WifiBasedHomeComingAwareComponent.class, LocationBasedHomeComingAwareComponent.class}, modules = HomeComingAwareModule.class)
public interface HomeComingAwareComponent {
    void inject(MainActivity activity);
}
```

### @Qualifier
동일한 인터페이스나 상위 클래스를 가지는 하위 클래스의 인스턴스에 대한 의존성을 제공할 때 사용됩니다. 예를 들면, 아래 코드와 같이 동일한 인터페이스를 구현한 두 가지 구현 클래스의 인스턴스에 대해 모두 의존성을 제공하고자 할때 이를 구분하기 위해 @WifiNetwork 이라는 custom annotation이 사용되고 있는데, 이는 @Qualifier annotation을 이용하여 정의된 custom annotation입니다.
```
@Qualifier
@Retention(RetentionPolicy.RUNTIME)
public @interface WifiNetwork {
}
```

```
@Module
public class WifiStateReceiverModule {
    @Provides @WifiNetwork
    WifiStateReceiver provideWifiNetworkStateReceiver() {
        Log.d(TAG, "provideWifiNetworkStateReceiver()");
        return new WifiNetworkStateReceiver();
    }

    @Provides @WifiSupplicant
    WifiStateReceiver provideWifiSupplicantStateReceiver() {
        return new WifiSupplicantStateReceiver();
    }
}
```


## 2. Dagger2 vs Injection class
Dagger2를 사용하는 것이 Dependency 생성을 한 곳에 모아서 해주는 Injection class를 사용하는 것에 비해 어떤 장점이 있을까?

Dependency를 제공받는 root 클래스의 인스턴스를 주입받을 수 없다
Injection class를 사용하면 아래와 같이 TasksPresenter는 직접 생성해야 함
```
// Create the presenter
mTasksPresenter = new TasksPresenter(
        Injection.provideUseCaseHandler(),
        tasksFragment,
        Injection.provideGetTasks(getApplicationContext()),
        Injection.provideCompleteTasks(getApplicationContext()),
        Injection.provideActivateTask(getApplicationContext()),
        Injection.provideClearCompleteTasks(getApplicationContext())
        );
```
반면, Dagger2와 같은 DI framework을 사용하면
```
@Inject TasksPresenter mTasksPresenter;
```
Injection.provideTasksPresenter를 추가하더라도 간결해질 뿐 dependency를 요청하는 곳에서 해당 dependency를 생성하는 것은 동일함
