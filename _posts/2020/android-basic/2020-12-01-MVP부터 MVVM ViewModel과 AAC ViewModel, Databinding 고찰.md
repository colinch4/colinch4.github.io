---
layout: post
title: "[안드로이드 기초] MVP부터 MVVM ViewModel과 AAC ViewModel, Databinding 고찰"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


MVP는 View와 Presenter가 1:1이고 결합도가 높다.

- Presenter에서는 View를 알고 이를 갱신하도록 유도한다.
- View는 Presenter로부터 View 갱신을 유도 받고, 이를 갱신한다.
- 이러한 이유로 View와 Presenter 간의 결합도가 높으며 의존관계를 깨기 어렵다.
- 1:1이기 때문에 딱 맞춰진 View와 Presenter간의 관계가 확실하게 보일 것이다.

MVVM은 MVP의 View와 Presenter의 높은 결합도를 줄이며, ViewModel에서 View를 모르도록 설계한다.

- ViewModel에서 View를 갱신할 때는 Observable 형태로 알리거나, Databinding을 통해 알려야한다.
- Databinding과 Observable을 통해 View의 갱신을 할 수 있도록 한다.
- ViewModel의 데이터가 수정되었더라도, View는 수정할게 없도록 설계할 수 있다.

AAC의 ViewModel은 일반적인 ViewModel에서 하지 않는 데이터 상태 유지와 Android Lifecycle을 내부에서 동작하도록 하고 있다.

MVP에서도 데이터바인딩을 사용할 수는 있다. Presenter를 Observable 형태의 데이터를 담고 있는 객체로 설정하고 XML에서 사용할 수 있다. 편할 수는 있다고 생각하는데 사용할거면 MVVM으로 사용하는게 나은 것 같다. 어차피 MVP에서는 View(Activity/Fragment)를 알고 있는데 XML까지 관여해서 뭔가 섞이는 느낌이 든다.

AAC의 ViewModel은 Databinding과 연계하기 편하게 만들어준 것 같다. ViewModel이 상태를 가지고 있기 때문에 화면 회전 등의 업데이트가 있을 때 상태를 가지고 있다가 Databinding을 해주면 된다. ViewModel은 Databinding과 연결하여 Observable 또는 LiveData를 쏴줄 수도 있고 포함된 뷰의 라이프사이클을 공유하기 때문에 뷰가 destroy 되었을 때 추가적인 조치를 취해줄 수 있다. 그래서 패턴에 상관없이 상태보존을 위해서 AAC의 ViewModel을 활용할 수 있을 것으로 보인다.

AAC의 ViewModel은 ViewModelProviders와 Factory를 활용하면 ViewModel이 여러 View에 연결될 수 있다는 원칙도 지킬 수 있게 해주는 것 같다. 그래서 AAC의 ViewModel은 MVVM의 ViewModel을 구현하면서도 안드로이드적으로 보다 구현을 할 수 있게 해주는 것 같다.

AAC의 ViewModel은 ViewModelProviders를 통해 Activity나 Fragment의 라이프사이클을 전달받고 따르게 된다. Databinding은 해당 ViewModel을 Binding Variable로 받고 XML에서 활용할 수 있도록 만든다. ViewModel에 있는 Observable, LiveData를 가져와서 View에 바로 적용하게 된다. 또는 이벤트를 전달하기도 한다. 여기에서 LiveData를 바인딩하고 싶다면 Activity나 Fragment를 LifecycleOwner로 만들어야 한다. 그러면 LiveData(LifeCycleObserver)는 Activity나 Fragment의 라이프사이클을 따르기 때문에 View가 Destroy되면 알아서 Observe 상태를 해지한다. 따라서 메모리 누수에 안전하고 백그라운드에서 View를 건드려서 앱이 죽는 문제가 사라지게 된다.

따라서 MVVM 통해 보다 효율적이라는 아키텍처를 구성한다는 말은 데이터의 공유만이 해당될 것이다. AAC ViewModel은 그저 액티비티나 프래그먼트의 라이프사이클을 따라가며 화면회전이나 종료에 반응하고 데이터를 공유해줄 수 있는 역할을 한다. MSDN의 ViewModel은 뷰를 몰라야한다! 그러나 AAC의 ViewModel은 액티비티의 라이프사이클을 알고 있어서 일종의 종속성이 생기게 된다. 이는 안드로이드의 특성을 반영한 것으로 액티비티가 종료될 때, 프래그먼트가 detach될 때 추가적인 구현을 해주기 위한 것으로 보인다. AAC ViewModel를 상속하여 구현된 MSDN의 ViewModel를 구현하고 싶은 ViewModel 안에 존재하는 LiveData(LifeCycleObserver)들은 독립적으로 액티비티나 프래그먼트에 전달되면서 DataBinding의 LifeCycleOwner를 따라가는 것이다. 상태가 보존되기 때문에 MSDN ViewModel을 따르면서도 안드로이드 적으로 좋은 코드가 탄생하는 것 같다.
