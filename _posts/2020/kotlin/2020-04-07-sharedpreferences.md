---
layout: post
title: "[Kotlin] SharedPreferences 데이터 공유"
date: 2020-04-07 15:15
category: 
author: kskim2
tags: [kotlin]
description: "데이터를 영구 저장하는 방법으로는 SharedPreferences(쉐어드프리퍼런스)가 있다. App에 포함되는 데이터 파일을 만들어서, 디바이스에 저장하는 방식이다.  `(key, value)`  형태로 저장/로드한다. 또한  `.edit()`  에디터를 이용해야 데이터의 수정, 삭제 등의 액션이 가능하다. 주로 ‘editor’라는 변수명에 저장해서 사용한다."
summary: 
---


## SharedPreferences

데이터를 영구 저장하는 방법으로는 SharedPreferences(쉐어드프리퍼런스)가 있다. App에 포함되는 데이터 파일을 만들어서, 디바이스에 저장하는 방식이다.  `(key, value)`  형태로 저장/로드한다. 또한  `.edit()`  에디터를 이용해야 데이터의 수정, 삭제 등의 액션이 가능하다. 주로 ‘editor’라는 변수명에 저장해서 사용한다.

`MainActivity`의  `onCreate`에서 쓸 수 있는 SharedPreferences 예제는 다음과 같다.

```kotlin
val pref = this.getPreferences(0)
val editor = pref.edit()
/* context.getPreferences의 SharedPreferences 인스턴스를 저장.
 * (0은 (Context.MODE_PRIVATE)와 같음)
 * 에디터를 호출해 editor로 초기화. */

 mainEt.setText(pref.getString("MessageKey", ""))
 /* mainEt(EditText)의 텍스트를 "MessageKey"에 해당하는 vaule로 설정.
  * 값을 불러오지 못했을 경우, default vaule는 ""로 지정. */

 mainBtn.setOnClickListener {
     editor.putString("MessageKey", mainEt.text.toString()).apply()
     /* mainBtn(Button) 클릭하면 "MessageKey"에 해당하는 String 데이터를 mainEt에서 불러와 저장. */

     val msg = pref.getString("MessageKey", "")
     if (msg == "") {
         Toast.makeText(this, "텍스트가 초기화되었습니다.", Toast.LENGTH_LONG).show()
     } else {
         Toast.makeText(this, "저장됨: $msg", Toast.LENGTH_LONG).show()
     }
     /* 값 저장 후 Toast 출력 */

```

  

![](https://blog.yena.io/assets/post-img/171218-01.JPG)  
텍스트를 저장한 후, 앱을 종료후 재실행 하거나 다시 Build하면 EditText에 저장했던 텍스트가 표시된다.  
  
![](https://blog.yena.io/assets/post-img/171218-02.JPG)  
앱을 재실행한 모습.  
  

  
  

**하지만, 이렇게 Activity마다 SharedPreferences를 초기화하는 것은 번거로운 일이다. 앱의 어디에서든 전역적으로 접근 가능하게 만드려면 새로 클래스를 생성하는 방법이 있다.**  
  

### SharedPreferences와 App 클래스 생성하기

이 방법은 크게 세 차례를 거친다.

1.  SharedPreferences Class 생성
2.  App Class 생성해서 SharedPreferences를 가장 먼저 쓸 수 있도록 설정
3.  manifest에 App Class의 이름 등록

우선 클래스 파일을 만들어 SharedPreferences에 필요한 변수를 만든다.

```kotlin
/* MySharedPreferences.kt */

class MySharedPreferences(context: Context) {

    val PREFS_FILENAME = "prefs"
    val PREF_KEY_MY_EDITTEXT = "myEditText"
    val prefs: SharedPreferences = context.getSharedPreferences(PREFS_FILENAME, 0)
    /* 파일 이름과 EditText를 저장할 Key 값을 만들고 prefs 인스턴스 초기화 */

    var myEditText: String
        get() = prefs.getString(PREF_KEY_MY_EDITTEXT, "")
        set(value) = prefs.edit().putString(PREF_KEY_MY_EDITTEXT, value).apply()
        /* get/set 함수 임의 설정. get 실행 시 저장된 값을 반환하며 default 값은 ""
         * set(value) 실행 시 value로 값을 대체한 후 저장 */
}

```

  

주의할 점! 이 SharedPreferences 클래스는 앱에 있는 다른 액티비티보다 먼저 생성되어야 다른 곳에 데이터를 넘겨줄 수 있다. 이 설정을 해주기 위해서는 App에 해당하는 Class 파일 또한 생성해주어야 한다.

```kotlin
/* App.kt */

class App : Application() {

    companion object {
        lateinit var prefs : MySharedPreferences
    }
    /* prefs라는 이름의 MySharedPreferences 하나만 생성할 수 있도록 설정. */

    override fun onCreate() {
        prefs = MySharedPreferences(applicationContext)
        super.onCreate()
    }
}

```

  
`Application()`을 상속받는 App 클래스를 생성, onCreate보다 먼저 prefs 초기화를 해준다. 그리고 이 액티비티의 이름을  `mainfest`의  `<application>`에 등록해준다.

```xml
<application
  ...
  android:name=".App"
  <activity ... />
</application>

```

  
  

여기까지 했으면 SharedPreferences를 사용할 준비가 끝났다. 메인 액티비티로 돌아가 프리퍼런스를 사용해보았다.

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mainEt.setText(App.prefs.myEditText)
        /* myEditText의 'get'이 실행됨 */

        mainBtn.setOnClickListener {
            App.prefs.myEditText = mainEt.text.toString()
            /* myEditText의 'set'이 실행됨 */

            val msg = App.prefs.myEditText
            if (msg == "") {
                Toast.makeText(this, "텍스트가 초기화되었습니다.", Toast.LENGTH_LONG).show()
            } else {
                Toast.makeText(this, "저장됨: $msg", Toast.LENGTH_LONG).show()
            }
            /* 값 저장 후 Toast 출력 */
        }

    }
}

```

  
  

![](https://blog.yena.io/assets/post-img/171218-03.JPG)

  

클래스로부터 데이터 불러오기에 성공했다.

SharedPreferences의 단점은  **App을 삭제한 후 재설치하면 SharedPreferences 파일도 같이 삭제되어**  데이터가 초기화된다는 것이다. 디바이스에 저장되는 것이 위험하다고 생각되면 서버에 저장하는 등, SharedPreferences가 아닌 다른 방법을 찾아야 할 것이다.

  
  

### References

-   [https://developer.android.com/training/data-storage/shared-preferences.html](https://developer.android.com/training/data-storage/shared-preferences.html)
-   [http://blog.teamtreehouse.com/making-sharedpreferences-easy-with-kotlin](http://blog.teamtreehouse.com/making-sharedpreferences-easy-with-kotlin)
-   [https://myprogrammingexperiments.wordpress.com/2017/06/04/manipulating-shared-prefs-with-kotlin-just-two-lines-of-code/](https://myprogrammingexperiments.wordpress.com/2017/06/04/manipulating-shared-prefs-with-kotlin-just-two-lines-of-code/)