---
layout: post
title: "[안드로이드 기초] Activity란"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


## Activity란?

안드로이드에서 가장 많이 쓰이는 Component로 주로 하는 일은 하나의 화면을 표현하는 것이다. 즉, **앱의 UI를 표현**하는 역할을 한다. 액티비티에는 Window가 있고, 그 Window에 텍스트나 이미지를 표시해 사용자 조작에 반응할 수 있도록 만들어졌다. 사용자가 조작을 하면서 발생하는 이벤트에 반응하기도 한다. 예를 들면 버튼을 클릭했을 때나 텍스트를 입력했을 때 발생하는 이벤트들이 그런 것이다. 개발자는 이러한 이벤트에 반응하는 동작을 지정해 줄 수 있다.

안드로이드 앱을 개발할 때 주로 사용하는 Activity Class에는 **Activity, FragmentActivity, AppCompatActivity**가 있다.

![](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/android-basic/images/Screen_Shot_2019-07-10_at_5-355fe374-873d-4ae0-a4db-1c154fcca8c7.36.01_PM.png?raw=true)

**Activity Class** - 안드로이드 버전의 기본 라이브러리 액티비티 클래스이며, 모든 다른 액티비티 클래스는 해당 클래스의 서브 클래스가 된다.

**FragmentActivity Class** - Fragment로 화면을 좀 더 쉽게 구성할 수 있도록 만든 Activity라고 한다.

**AppCompatActivity Class** - Activity와 FragmentActivity 모두를 상속 받은 클래스이다. 따라서 Acitivity 기본 기능과 더불어 Fragment도 쉽게 사용할 수 있는 Activity이다. Material Design의 ActionBar를 쓰기 위한 확장된 개념의 Activity이고 Material Design 가이드라인에 따른 AppCompat 라이브러리를 제대로 활용할 수 있다고 한다. 요즘에는 주로 해당 Activity를 사용하기를 권장받는다. 

실제로 프로젝트에서도 AppCompatActivity를 확장받아서 BaseActivity를 만들고 프로젝트를 진행했었다. MVVM 패턴을 사용했던 프로젝트였기 때문에 DataBinding과 ViewModel을 제네릭을 활용하여 Activity에서 활용할 타입을 정해두었다.

```Java
public abstract class BaseActivity<T extends ViewDataBinding, V extends BaseViewModel> extends AppCompatActivity
    implements BaseFragment.Callback {

        //...

}
```

## Activity의 UI 구현

안드로이드 Activity가 화면에 UI를 보여주기는 하지만 직접 그리는 기능을 수행하여 화면을 그리는 것은 아니다. UI는 뷰 계층, 즉 View 클래스에서 파생된 객체가 제공한다. 각 View는 Activity 창 안의 특정한 직사각형 공간을 제어하며 사용자 상호작용에 대응 할 수 있다. Activity는 이러한 View 또는 ViewGroup의 다양한 조합을 화면에 배치함으로써 UI를 구현한다.

뷰를 생성할 때는 XML으로 기술하는 방법과 자바 코드로 기술하는 방법이 있다. 기본적으로 XML로 기술하는 것이 자바 코드보다 코드 양도 적고 읽기에도 편해 유지 및 관리에도 유리하다. Activity가 화면에 표현할 UI는 Layout 리소스 XML 파일(R.layout.XXX)이거나, android.view.View에서 상속받은 클래스(TextView, Button, ...) 이어햐 하며, setContentView() 함수를 통해 화면에 출력될 Layout 리소스 XML ID 또는 View 클래스를 지정할 수 있다. 이러한 관점에서 보면 Acitivty는 화면에 UI를 표시하기 위한 툴이라는 개념도 된다.

- "위젯"이란 화면에 시각적(및 대화형) 요소를 제공하는 뷰이다. 예를 들어 버튼, 텍스트 필드, 체크박스나 그저 하나의 이미지일 수도 있습니다.
- "레이아웃"은 선형 레이아웃, 격자형 레이아웃, 상대적 레이아웃과 같이 하위 레이아웃에 대해 독특한 레이아웃 모델을 제공하는 ViewGroup에서 파생된 뷰이다.

```kotlin
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```
    

## Activity 시작

다른 Activity를 시작하려면 startActivity()를 호출한 다음 이에 시작하고자 하는 액티비티를 설명하는 Intent를 전달하면 된다. (명시적 인텐트)
```Java
Intent intent = new Intent(this, SignInActivity.class);
startActivity(intent);
```
Intent를 처리할 수 있는 Activity가 여러 개 있는 경우, 사용자가 어느 것을 사용할지 선택하도록 할 수 있다. (암시적 인텐트)

```Java
Intent intent = new Intent(Intent.ACTION_SEND);
intent.putExtra(Intent.EXTRA_EMAIL, recipientArray);
startActivity(intent);
```
### 결과에 대한 Activity 시작

startActivityForResult()를 호출해서 액티비티를 시작한다. 그런 다음 후속 액티비티에서 결과를 받으려면, onActivityResult() 콜백 메서드를 구현한다. 해당 후속 액티비티가 완료되면, 이것이 Intent 형식으로 결과를 onActivityResult() 메서드에 반환한다.

```Java
private void pickContact() {
    // Create an intent to "pick" a contact, as defined by the content provider URI
    Intent intent = new Intent(Intent.ACTION_PICK, Contacts.CONTENT_URI);
    startActivityForResult(intent, PICK_CONTACT_REQUEST);
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    // If the request went well (OK) and the request was PICK_CONTACT_REQUEST
    if (resultCode == Activity.RESULT_OK && requestCode == PICK_CONTACT_REQUEST) {
        // Perform a query to the contact's content provider for the contact's name
        Cursor cursor = getContentResolver().query(data.getData(),
        new String[] {Contacts.DISPLAY_NAME}, null, null, null);
        if (cursor.moveToFirst()) { // True if the cursor is not empty
            int columnIndex = cursor.getColumnIndex(Contacts.DISPLAY_NAME);
            String name = cursor.getString(columnIndex);
            // Do something with the selected contact's name...
        }
    }
}
```

## Activity 종료

액티비티를 종료하려면 해당 액티비티의 finish() 메서드를 호출하면 된다. finishActivity()를 호출하여 이전에 시작한 별도의 액티비티를 종료할 수도 있다.

하지만 구글에서는 이러한 함수의 직접적인 사용을 권장하지 않고 있다. 이는 안드로이드 시스템이 관리하는 Activity의 생명 주기에 영향을 줄 수 있기 때문이다.
