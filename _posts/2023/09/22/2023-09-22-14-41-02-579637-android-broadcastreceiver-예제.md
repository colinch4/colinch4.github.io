---
layout: post
title: "android broadcastreceiver 예제"
description: " "
date: 2023-09-22
tags: [Android, BroadcastReceiver]
comments: true
share: true
---

안드로이드에서 Broadcast Receiver는 앱 간에 메시지를 주고받는 데 사용되는 컴포넌트입니다. BroadcastReceiver는 시스템이나 다른 앱에서 발송한 브로드캐스트 메시지를 수신하고 특정 작업을 수행할 수 있습니다. 이번 예제에서는 간단한 BroadcastReceiver의 구현 방법을 알아보겠습니다.

## 1. BroadcastReceiver 클래스 생성

```
public class MyReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        // 브로드캐스트 메시지를 수신했을 때 실행되는 메서드
        // 원하는 작업을 수행하면 됩니다.
    }
}
```

위의 코드에서 `MyReceiver`는 BroadcastReceiver를 상속하는 클래스입니다. `onReceive()` 메서드는 브로드캐스트 메시지를 수신했을 때 실행되는 메서드로, 여기에서는 원하는 작업을 수행하면 됩니다.

## 2. AndroidManifest.xml에 BroadcastReceiver 등록

```
<receiver
    android:name=".MyReceiver"
    android:enabled="true"
    android:exported="true">
    <intent-filter>
        <action android:name="com.example.myapp.ACTION_CUSTOM_EVENT" />
    </intent-filter>
</receiver>
```

위의 코드에서 `MyReceiver` 클래스를 `<receiver>` 태그로 AndroidManifest.xml에 등록합니다. `android:name` 속성에는 `MyReceiver`의 패키지 경로를 입력합니다. `<intent-filter>` 태그 안에는 해당 BroadcastReceiver가 수신할 브로드캐스트 메시지의 액션을 등록합니다.

## 3. 브로드캐스트 메시지 발송

```
Intent intent = new Intent("com.example.myapp.ACTION_CUSTOM_EVENT");
context.sendBroadcast(intent);
```

위의 코드는 `com.example.myapp.ACTION_CUSTOM_EVENT` 액션을 가진 브로드캐스트 메시지를 발송하는 코드입니다. `sendBroadcast()` 메서드를 사용하여 브로드캐스트 메시지를 발송할 수 있습니다.

## 4. 메시지 수신

위의 코드에서 등록한 브로드캐스트 메시지를 `MyReceiver` 클래스에서 수신하여 특정 작업을 수행할 수 있습니다. `onReceive()` 메서드 안에 원하는 작업을 구현하면 됩니다.

위의 예제를 참고하여 원하는 작업을 하는 BroadcastReceiver를 구현해보세요!

## 마무리

이번 블로그 포스트에서는 안드로이드에서의 BroadcastReceiver 예제를 살펴보았습니다. BroadcastReceiver를 사용하면 앱 간에 메시지를 주고받을 수 있으므로 다양한 앱 개발 시나리오에 유용하게 사용할 수 있습니다.

#Android #BroadcastReceiver