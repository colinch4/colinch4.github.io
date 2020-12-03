---
layout: post
title: "[dagger] Dependency Injection with Dagger2"
description: " "
date: 2020-12-03
tags: [dagger]
comments: true
share: true
---


## 1. Dependency Injection
Dependency Injection(의존성 주입)을 하려면 먼저 dependency에 대해 알아야 함

#### 의존성(dependency)
- 의존성은 두 모듈 사이의 coupling(결합)을 말함
>**A dependency is a coupling between two modules of our code** (in oriented object languages, two classes), usually because one of them uses the other to do something.

- 하나의 클래스에서 다른 클래스을 사용할 때 직접 인스턴스를 생성할 때 높은 의존성이 발생함

#### 의존성의 위험성
- 하나의 모듈을 수정하면 결합된(coupled) 다른 모듈도 수정해야 됨
- 테스트 가능한 앱을 만들기 힘들어짐  
  unit test에서는 모듈을 테스트하기 위해서는, 해당 모듈을 다른 모듈들로부터 고립(isolated)시켜야 함

#### 어떻게 의존성을 해결?
모듈 내에서 다른 모듈에 대한 객체를 생성하지 못하도록 하려면, 다른 방법으로 객체를 제공해야 됨  
How?
- 생성자를 통해 통해 객체를 전달  
  기본적으로 dependency inversion principle이 의미하는 바와 동일함
- Concrete modules의 객체에 의존해서는 안되고, 추상화해야 됨(using interface or abstract class)  
![](http://fernandocejas.com/wp-content/uploads/2015/04/dependency_inversion1.png)


#### 의존성 주입(Dependency Injection, DI)
- 의존성(dependency)를 전달하는 것
- 다른 모듈에서 사용하는 모듈을 직접 생성하는 일을 외부로 추출하기 위함
- 프로그래밍에서 구성요소간의 종속성을 소스코드에서 설정하지 않고 외부의 설정파일 등을 통해 주입하도록 하는 디자인 패턴 중의 하나이다.

#### Problem
- 모듈 내에서 객체를 생성할 수 없다면, 모듈 외부에 객체를 생성하는 곳이 필요함
- 생성하려는 객체가 여러 의존성을 가질 경우 많은 boilerplate code들로 코드가 지저분해짐


#### Dependency injector(or DI framework)?
- 앱 내에서 하나의 포인트에서 모듈들의 인스터스들 생성해서 의존성을 주입하는 역할을 함  
>We can consider it as another module in our app that is in charge of providing instances of the rest of modules and inject their dependencies. That is basically its duty. The creation of modules is localized in a single point in our app, and we have full control over it.

#### 지금까지의 내용을 예제를 통해 쉽게 다시 복습
  <http://www.slideshare.net/baejjae93/dependency-injection-36867592>


#### 의존성 주입의 중요한 장점들
- 모듈들간의 결합도 를 낮출 수 있음
- 코드 재사용을 높여서 작성된 모듈을 여러 곳에서 소스코드의 수정 없이 사용할 수 있음.
- 모의 객체 등을 이용한 단위 테스트의 편의성을 높여준다.


## 2. Dependency Injection with Dagger2

#### What is Dagger?
Dagger는 low-end devices를 위해 설계된 dependency injector.
- **No reflection**  
  대부분의 injector들은 dependency를 생성하고 주입하기 위해 reflection을 사용하지만, dagger는 pre-compiler를 이용해 의존성 주입에 필요한 모든 class들을 생성함
- 가장 powerful하진 않지만, 가장 효율적이라고 함  
- 다른 DI framework들은 runtime에 dependency들을 분석하지만, dagger는 compile time에 의존성을 분석하고 의존성을 엮기 위한 코드를 생성함
- 의존성 주입을 위해 Java의 표준 어노테이션(JSR-330)을 사용함

#### JSR-330 이란?

‘Dependency Injection for Java’는 재사용 확대, 자바 코드의 테스트 가능성과 유지 가능성을 위해 표준 어노테이션들을 정의했습니다. Dagger 1 과 2 모두 이 표준을 사용해서 일관성을 유지하고, 의존성 주입의 표준 방법을 제공함

#### Dagger2 API

##### @Inject annotation
- JSR-330 표준 annotation으로 의존성을 요청함. DI framework(Dagger2)로 부터 제공받아야 되는 의존성을 표기함
- Dagger2는 세 가지 방식의 의존성 주입을 제공함  

  1. Constructor injector  
```Java
  public class LoginActivityPresenter {

      private LoginActivity loginActivity;
      private UserDataStore userDataStore;
      private UserManager userManager;

      @Inject
      public LoginActivityPresenter(LoginActivity loginActivity,
                                    UserDataStore userDataStore,
                                    UserManager userManager) {
          this.loginActivity = loginActivity;
          this.userDataStore = userDataStore;
          this.userManager = userManager;
      }
  }
```
  2. Field injector  
```
  public class SplashActivity extends AppCompatActivity {

      @Inject
      LoginActivityPresenter presenter;
      @Inject
      AnalyticsManager analyticsManager;

      @Override
      protected void onCreate(Bundle bundle) {
          super.onCreate(bundle);
          getAppComponent().inject(this);
      }
  }  
```
  3. Method injector  
```
  public class LoginActivityPresenter {

      private LoginActivity loginActivity;

      @Inject
      public LoginActivityPresenter(LoginActivity loginActivity) {
          this.loginActivity = loginActivity;
      }

      @Inject
      public void enableWatches(Watches watches) {
          watches.register(this);    //Watches instance required fully constructed LoginActivityPresenter
      }
  }
```


#### @Module annotation
모듈들은 의존성을 제공하는 메서드들을 가진 클래스입니다. 의존성을 제공하는 클래스를 정의하고 @Module 어노테이션을 답니다. 그러면 Dagger 는 클래스 인스턴스를 만들 때 의존성을 만족시키기 위한 정보를 찾을 수 있습니다.

#### @Provide annotation
모듈 안에서 해당 어노테이션이 달린 메서드를 정의합니다. 해당 어노테이션이 달린 메서드가 Dagger 가 어떻게 의존성에 맞게 객체를 만들고 제공하는지 알려줍니다.

#### @Component annotation
컴포넌트는 @Inject 와 @Module 사이 다리이며 의존성을 주입하는 역할을 합니다. 컴포넌트는 미리 정의한 모든 타입의 인스턴스를 줍니다. @Component 어노테이션은 인터페이스에다만 달아야합니다 그리고 컴포넌트를 구성하는 모든 @Module 이 달린 클래스 목록을 적어야합니다. 컴포넌트에서 사용하는 모듈들중 하나라도 없다면 컴파일 타임에 에러를 만듭니다. 모든 컴포넌트들은 컴포넌트에 포함된 모듈들을 통해 의존성의 범위를 알 수 있습니다.

#### @Scope annotation
스코프는 매우 유용하고 Dagger 2 에서 사용자 정의 어노테이션을 통해 범위를 나누는 명확한 방법입니다. 나중에 예제에서 보겠지만 이것은 매우 강력한 기능입니다. 앞에서 언급한바와 같이 하기 때문에, 모든 객체는 자기 자신의 인스턴스를 관리하는 방법에 대해 알필요가 없습니다. 예를들어 사용자가 지정한 @PerActivity 어노테이션이 달려있는 클래스는 액티비티가 살아있는 동안 존재합니다. 다시말하자면 객체 범위의 단위를 정의할 수 있습니다.


**참고자료**  
<http://frogermcs.github.io/dependency-injection-with-dagger-2-the-api/>


### Setup

Android Studio by default will not recognize a lot of generated Dagger 2 code as legitimate classes, but adding the android-apt plugin will add these files into the IDE class path and enable you to have more visibility. Add this line to your root build.gradle:

```
 dependencies {
     // other classpath definitions here
     classpath 'com.neenbedankt.gradle.plugins:android-apt:1.8'
 }
```
Then make sure to apply the plugin in your app/build.gradle:

```
// add after applying plugin: 'com.android.application'  
apply plugin: 'com.neenbedankt.android-apt'
```

Add these three lines to your app/build.gradle file after this apply statement:  

```
dependencies {
    // apt command comes from the android-apt plugin
    apt 'com.google.dagger:dagger-compiler:2.5'
    compile 'com.google.dagger:dagger:2.5'
    provided 'javax.annotation:jsr250-api:1.0'
}
```



### 참고 자료
- <https://speakerdeck.com/jakewharton/dependency-injection-with-dagger-2-devoxx-2014>

- <https://speakerdeck.com/frogermcs/dependency-injection-with-dagger-2>

- <https://guides.codepath.com/android/Dependency-Injection-with-Dagger-2#advantages>

- <https://speakerdeck.com/frogermcs/dependency-injection-with-dagger-2>

- <http://frogermcs.github.io/dependency-injection-with-dagger-2-introdution-to-di/>

- <http://frogermcs.github.io>
- <https://medium.com/@jason_kim/tasting-dagger-2-on-android-%EB%B2%88%EC%97%AD-632e727a7998#.p8iepei2v>
