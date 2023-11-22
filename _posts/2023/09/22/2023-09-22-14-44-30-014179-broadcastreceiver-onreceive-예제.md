---
layout: post
title: "broadcastreceiver onreceive 예제"
description: " "
date: 2023-09-22
tags: [android]
comments: true
share: true
---

`BroadcastReceiver`는 안드로이드에서 시스템에서 발생하는 다양한 이벤트를 수신하는 역할을 합니다. 이벤트 발생시 `onReceive` 메소드가 호출되어 이벤트에 대한 처리를 수행합니다. 

아래 예제는 장치 부팅 시 `ACTION_BOOT_COMPLETED` 액션을 수신하는 `BroadcastReceiver`를 구현한 예제입니다.

```java
public class BootReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        String action = intent.getAction();
        
        if (action.equals(Intent.ACTION_BOOT_COMPLETED)) {
            // 부팅 시 처리할 작업 수행
            // 예: 앱 초기화, 서비스 시작 등
            Toast.makeText(context, "장치 부팅 완료", Toast.LENGTH_SHORT).show();
        }
    }
}
```

위 코드에서 `BootReceiver` 클래스는 `BroadcastReceiver`를 상속하고 `onReceive` 메소드를 구현합니다. `onReceive` 메소드는 브로드캐스트 이벤트를 수신하게 되면 호출되며, 파라미터로는 현재 `Context`와 `Intent` 객체가 전달됩니다.

`Intent` 객체를 통해 받은 액션을 확인하고, `ACTION_BOOT_COMPLETED` 액션이 수신되었을 경우 부팅 완료 메시지를 보여줍니다.

이제 이 `BroadcastReceiver`를 등록하고 부팅 완료 이벤트를 수신할 수 있습니다. `AndroidManifest.xml` 파일에서 아래와 같이 등록해야 합니다.

```xml
<manifest ...>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    
    <application ...>
        <receiver
            android:name=".BootReceiver"
            android:enabled="true"
            android:exported="true" >
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
            </intent-filter>
        </receiver>
    </application>
</manifest>
```

`<uses-permission>` 태그를 통해 `RECEIVE_BOOT_COMPLETED` 퍼미션을 요청하고, `<receiver>` 태그에서 `BootReceiver` 클래스를 등록하고 `BOOT_COMPLETED` 액션을 필터링합니다. 이제 장치 부팅 시 해당 `BroadcastReceiver`가 작동할 준비가 끝났습니다.

위 예제 코드를 참고하여 필요한 액션에 따라 `BroadcastReceiver`를 구현하고 적절한 처리 로직을 작성하면 다양한 이벤트를 수신하고 처리할 수 있습니다.

#Android #BroadcastReceiver