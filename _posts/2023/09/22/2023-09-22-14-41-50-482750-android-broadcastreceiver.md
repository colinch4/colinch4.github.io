---
layout: post
title: "android broadcastreceiver"
description: " "
date: 2023-09-22
tags: [BroadcastReceiver]
comments: true
share: true
---

안드로이드에서 Broadcast Receiver(브로드캐스트 리시버)는 안드로이드 시스템이나 다른 앱으로부터 전달되는 broadcast 메시지(브로드캐스트 메시지)를 수신하는 컴포넌트입니다. 이러한 메시지는 시스템 이벤트, 앱 간 통신, 다양한 장치 또는 센서 상태 변경과 같은 다양한 이벤트를 나타낼 수 있습니다. Broadcast Receiver는 앱의 특정 이벤트를 처리하고, 필요한 동작을 수행하거나 데이터를 처리할 수 있는 기능을 제공합니다.

# 안드로이드 Broadcast Receiver의 등록과 사용 방법

## 1. Manifest 파일에서 Broadcast Receiver 등록

Broadcast Receiver를 사용하려면 먼저 앱의 AndroidManifest.xml 파일에 등록해야 합니다. 다음은 예시입니다.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp">

    <application
        ...>

        <receiver
            android:name=".MyBroadcastReceiver"
            android:enabled="true"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MY_ACTION" />
                <!-- 추가적인 필터 등록 가능 -->
            </intent-filter>
        </receiver>
        
    </application>

</manifest>
```
위의 코드에서는 `MyBroadcastReceiver`라는 클래스를 Broadcast Receiver로 등록했습니다. `android.intent.action.MY_ACTION`이라는 액션을 필터로 등록했으며, 이 액션을 가진 broadcast 메시지를 수신할 수 있습니다. 필터에 추가적인 액션 또는 데이터 등을 등록하여 더 특정한 메시지만 수신할 수 있습니다.

## 2. Broadcast Receiver 클래스 구현

Broadcast Receiver 클래스를 구현하여 broadcast 메시지를 수신하고 처리할 수 있습니다. 다음은 예시입니다.

```java
public class MyBroadcastReceiver extends BroadcastReceiver {
    
    @Override
    public void onReceive(Context context, Intent intent) {
        String action = intent.getAction();
        if (action != null && action.equals("android.intent.action.MY_ACTION")) {
            // 액션에 따른 처리
            // ...
        }
    }
    
}
```
위의 코드에서는 `MyBroadcastReceiver` 클래스가 `BroadcastReceiver`를 상속받아 구현되었습니다. `onReceive()` 메소드는 broadcast 메시지를 수신한 경우 호출되며, 액션에 따라 특정 처리를 할 수 있습니다. 위의 예시에서는 `android.intent.action.MY_ACTION` 액션을 처리하는 코드를 작성하였습니다.

## 3. Broadcast Receiver 등록 및 등록 해제

Broadcast Receiver를 등록하려면 앱의 실행 중인 컨텍스트에서 `registerReceiver()` 메소드를 사용하여 등록해야 합니다. 등록 후에는 broadcast 메시지를 받을 수 있습니다. 등록 해제는 앱이 더 이상 broadcast 메시지를 수신하지 않을 때 수행됩니다.

```java
// Broadcast Receiver 등록
MyBroadcastReceiver receiver = new MyBroadcastReceiver();
IntentFilter filter = new IntentFilter();
filter.addAction("android.intent.action.MY_ACTION");

context.registerReceiver(receiver, filter);

// Broadcast Receiver 등록 해제
context.unregisterReceiver(receiver);
```

# 안드로이드 Broadcast Receiver의 활용 예시

안드로이드 Broadcast Receiver는 다양한 상황에서 활용될 수 있습니다. 몇 가지 예시를 살펴보겠습니다.

1. 네트워크 상태 변경 감지하기
- `android.net.conn.CONNECTIVITY_CHANGE` 액션을 필터로 등록하여 네트워크 상태 변경을 감지하고 처리할 수 있습니다.

2. 배터리 상태 변경 감지하기
- `android.intent.action.BATTERY_CHANGED` 액션을 필터로 등록하여 배터리 상태 변경을 감지하고 처리할 수 있습니다.

3. 외부 브로드캐스트 메시지 수신하기
- 시스템에서 제공하는 broadcast 메시지뿐만 아니라 다른 앱에서 발생하는 브로드캐스트 메시지를 수신하여 처리할 수 있습니다.

이처럼 안드로이드 Broadcast Receiver는 다양한 상황에서 유용하게 사용될 수 있으며, 다른 앱과의 상호작용이나 앱 내부의 이벤트 처리를 위해 중요한 기능입니다.

#안드로이드 #BroadcastReceiver