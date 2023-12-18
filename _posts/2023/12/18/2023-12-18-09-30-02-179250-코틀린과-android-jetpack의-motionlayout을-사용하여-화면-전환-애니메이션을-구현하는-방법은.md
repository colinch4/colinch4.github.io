---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 MotionLayout을 사용하여 화면 전환 애니메이션을 구현하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

아래는 간단한 예제 코드입니다. 

```kotlin
// activity_main.xml

<?xml version="1.0" encoding="utf-8"?>
<MotionLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:motion="http://schemas.android.com/apk/res-auto"
    android:id="@+id/motionLayout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    motion:layoutDescription="@xml/motion_scene">

    <View
        android:id="@+id/view"
        android:layout_width="match_parent"
        android:layout_height="200dp"
        android:background="#FF5722"/>

</MotionLayout>
```

```xml
// res/xml/motion_scene.xml

<?xml version="1.0" encoding="utf-8"?>
<MotionScene 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <Transition
        app:constraintSetStart="@id/start"
        app:constraintSetEnd="@id/end">
        
        <KeyFrameSet>
            <KeyPosition
                app:framePosition="20"
                app:percentX="1"
                app:percentY="0" />
        </KeyFrameSet>

    </Transition>

    <ConstraintSet android:id="@+id/start">
        <Constraint
            android:id="@+id/view"
            android:layout_width="0dp"
            android:layout_height="200dp"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintTop_toTopOf="parent"/>
    </ConstraintSet>

    <ConstraintSet android:id="@+id/end">
        <Constraint
            android:id="@+id/view"
            android:layout_width="0dp"
            android:layout_height="200dp"
            app:layout_constraintStart_toEndOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintTop_toTopOf="parent"/>
    </ConstraintSet>

</MotionScene>
```

이제, 액티비티나 프래그먼트에서 MotionLayout을 초기화하고 전환을 시작하도록 코드를 추가하면 됩니다.

```kotlin
// MainActivity.kt

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val motionLayout = findViewById<MotionLayout>(R.id.motionLayout)
        motionLayout.transitionToState(R.id.end)
    }
}
```

이렇게하면 화면 전환 애니메이션이 구현될 것입니다! MotionLayout을 사용하면 더 많은 복잡한 애니메이션도 구현할 수 있으며, XML 레이아웃 파일을 사용하여 애니메이션을 정의하므로 코드가 간결해지고 유지보수가 쉬워집니다.

더 많은 MotionLayout 및 Android Jetpack에 대한 정보는 <https://developer.android.com/training/constraint-layout/motionlayout>를 참조하세요.