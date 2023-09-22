---
layout: post
title: "broadcastreceiver android 예제"
description: " "
date: 2023-09-22
tags: [Android, BroadcastReceiver]
comments: true
share: true
---

Android에서 Broadcast Receiver는 앱 간의 통신을 가능하게하는 강력한 기능입니다. Broadcast Receiver를 사용하여 특정 이벤트를 감지하고 해당 이벤트에 대한 작업을 수행할 수 있습니다. 이 예제에서는 Android 앱에서 Broadcast Receiver를 구현하는 방법을 안내합니다.

1. 먼저, AndroidManifest.xml 파일을 열고 다음 코드를 추가하여 BroadcastReceiver를 선언합니다.
```xml
<receiver
    android:name=".MyBroadcastReceiver"
    android:enabled="true"
    android:exported="true">
    <intent-filter>
        <action android:name="com.example.broadcast.MY_ACTION" />
    </intent-filter>
</receiver>
```

2. 다음으로, BroadcastReceiver를 구현하는 Java 클래스를 작성합니다. 이 예제에서는 MyBroadcastReceiver 클래스를 사용합니다.
```java
public class MyBroadcastReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent.getAction() != null && intent.getAction().equals("com.example.broadcast.MY_ACTION")) {
            // Broadcast 이벤트가 수신되었을 때 수행할 작업을 여기에 작성합니다.
            // 예를 들어, Toast 메시지를 표시할 수 있습니다.
            Toast.makeText(context, "Broadcast Received", Toast.LENGTH_SHORT).show();
        }
    }
}
```

3. Broadcast 이벤트를 발송하는 액티비티나 서비스에서 다음 코드를 사용하여 Broadcast를 보낼 수 있습니다.
```java
Intent intent = new Intent("com.example.broadcast.MY_ACTION");
sendBroadcast(intent);
```

위 예제에서는 "com.example.broadcast.MY_ACTION"이라는 사용자 정의 액션을 사용했습니다. 이를 개발자가 원하는대로 수정할 수 있습니다.

이 예제를 통해 Android에서 Broadcast Receiver를 구현하는 방법을 알아보았습니다. Broadcast Receiver를 사용하여 앱 간의 통신을 간편하고 효율적으로 구현할 수 있습니다. 이 기능을 활용하여 Android 앱의 기능을 확장할 수 있습니다.

#Android #BroadcastReceiver