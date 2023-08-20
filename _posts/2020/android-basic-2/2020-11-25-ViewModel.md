---
layout: post
title: "[안드로이드] ViewModel 이란"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---


## 뷰 모델 (ViewModel)
  
  
  뷰 모델은 ui관련 데이터를 라이프 사이클에 관계없이 저장하고 관리하기 위한 클래스이다.
  
  라이프 사이클에 관련이 없으므로 화면 회전이나, 폰트 변경 등 설정이 변경되어 액티비티가 다시 실행되더라도
  
  데이터가 유지된다.
  
  new 키워드로 객체가 생성하면 안되고 반드시 ViewModelProvider를 통해 객체를 생성해야한다.


## 뷰 모델 내부
  
  내부적으로 Holder 프래그먼트가 사용되며, ViewModelProvider가 HolderFragment를 생성해 액티비티에 추가합니다.
  
  이 HolderFragment가 ViewModel을 멤버 변수로 관리하며, setRetainInstance(true)로 프래그먼트를 유지하는 기법을 사용한다.
  
  ```
  @RestrictTo(RestrictTo.Scope.LIBRARY_GROUP)
  public class HolderFragment extends Fragment {
    public HolderFragment() {
        setRetainInstance(true);
    }
    ...
  }
  ```
  
  이런 점에서 ViewModel은 Retained Fragment의 연장선에 있는 라이브러리이다.
  

## 뷰 모델 구현
  
  UI컨트롤러에 ViewModel 클래스를 제공한다. 뷰 모델 객체는 구성이 변경되는 동안 자동으로 보관되므로, 
  
  이러한 객체가 보유한 데이터는 다음 액티비티나 프래그먼트 인스턴스에서 즉시 사용할 수 있다.
  
  뷰모델은 추상클래스이며, 이 클래스를 상속하는 것만으로 ViewModel을 만들 수 있습니다.
  
  ```
  class myViewModel : ViewModel(){
    override fun onCleared(){
      // clean up code
    }
  }
  ```
  
  위와 같이 뷰 모델을 정의하고, 아래와 같이 액티비티  or 프래그먼트에서 뷰모델을 싱글톤으로 가져온다.
  
  ```
  class MyActivity: AppCompatActivity(){
    
    overrride fun onCreate(saveInstanceState: Bundle?){

      val model = ViewModelProvider(this).get(MyViewModel::class.java) // lifecycle extension을 이용한 방법
      
      //val model = ViewModelProvider(this, ViewModelProvider.NewInstanceFactory()).get(MyViewModel::class.java)  -> lifecycle extension 없이 가능한 방법. 
      
      //val model = ViewModelProviders.of(this).get(myViewModel::class.java) -> 현재는 deprecated 된 방법
      
      })
    }
  }
  ```
  
  액티비티가 다시 생성되면 동일한 뷰모델 인스턴스를 받는다.
  
  관련 액티비티가 destroy되면 리소스를 정리할 수 있더록 ViewModel 객체의 onCleared() 메서드를 호출한다.
  
  #### ※ 뷰 모델은 뷰, 라이프 사이클 또는 액티비티의 컨텍스트를 참조하는 클래스를 참조해서는 안된다!!
  
  이러한 이유는 뷰 모델이 종료된 액티비티의 참조를 가지고 있게 되면서 메모리 릭이 발생하기 때문이다.
  
  단, 어플리케이션의 컨텍스트는 뷰모델에서 가져도 된다. 어플리케이션은 어플리케이션의 생명주기를 따르기 때문이다.
  
  
## 뷰 모델의 생명 주기
  
  뷰 모델 객체의 범위는 뷰 모델을 가져올 때 ViewModelProvider에 전달되는 Lifecycle로 지정된다.
  
  뷰 모델은 액티비티에서는 액티비티가 끝날 때 까지, 프래그먼트라면 프래그먼트가 분리될 때 까지 메모리에 남아 다.
  
  일반적으로는 시스템에서 액티비티의 onCreate 메서드를 처음 호출할 때 뷰 모델을 요청한다.
  
  
## LiveData와 함께 사용하기
  
  
  1. 뷰모델 작성
  
  ```
  class myViewModel : ViewModel(){
  
    val counter : MutableLiveData<Integer> by lazy { 
        MutableLiveData<Integer>()
    }
  }
  
  ```
  
  2. 액티비티 작성
  
  ```
  class MyActivity: AppcompatActivity(){
    
    private lateinit var model: myViewModel
    
    override fun onCreate(savedInstanceState : Bundle?){
      super.onCreate(savedInstanceState)
      
      //모델 가져오기
      model = ViewModelProvider(this).get(myViewModel::class.java)
      
      // ui 갱신
      val observer = Observer<String>{ newCounter->
        counterTextView.text = newCounter        
      }
      
      
      //livedata를 observe함. 라이프사이클 오너로서 액티비티를 전달하고 옵저버를 전달.
      model.counter.observe(this, observer)
    }
  }
  ```


  
  
