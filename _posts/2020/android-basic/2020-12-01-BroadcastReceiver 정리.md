---
layout: post
title: "[안드로이드 기초] BroadcastReceiver 정리"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


안드로이드 앱은 publish-subscribe 디자인 패턴과 비슷하게, 안드로이드 시스템이나 다른 안드로이드 앱으로부터 브로드캐스트 메시지를 받거나 보낼 수 있다. 브로드캐스트는 어떤 이벤트가 발생했을 때 보내진다. 예를 들어, 안드로이드 시스템은 시스템이 부팅되었을 때, 디바이스가 충전을 시작했을 때 관련 브로드캐스트를 보낼 수 있고, 앱은 새로운 데이터가 다운로드 됐다거나 하는 상황에 브로드캐스트를 보낼 수 있다.

앱들은 특정한 브로드캐스트를 받기 위해 리시버를 등록할 수 있다. 그러나 브로드캐스트를 받고 작업을 백그라운드에서 처리하는 상황을 남용해서는 안된다. 이는 시스템 성능을 저하시킬 수 있다.

순차적으로 실행되기 때문에 한꺼번에 너무 많은 Broadcast가 처리되도록 하면 안된다. 오래 대기하면 안된다. ANR 발생한다. 최대한 간단한 작업만 하도록 해야한다.

브로드캐스트 메시지는 Intent 객체에 감싸져 있고 인텐트는 android.intent.action.AIRPLANE_MODE와 같은 액션을 담고 있다.

브로드캐스트에는 안드로이드 버전마다 큼직한 변화들이 있어왔다.

**Android 9**

NETWORK_STATE_CHANGED_ACTION 브로드캐스트는 더 이상 유저의 위치나 개인 식별 정보에 대한 정보를 받지 않는다. 이외에 Wi-Fi로부터의 브로드캐스트는 SSIDs, BSSIDs, 연결 정보 등을 제공하지 않는다. 대신에 getConnectionInfo()를 사용해야한다.

**Android 8.0**

대부분의 정적 리시버를 사용할 수 없게 되었다. 동적 리시버를 사용하도록 권장된다.

**Android 7.0**

- ACTION_NEW_PICTURE
- ACTION_NEW_VIDEO

위의 시스템 브로드캐스트가 작동하지 않는다.

또한 CONNECTIVITY_ACTION 브로드캐스트는 동적 리시버로만 등록해야한다.

## 브로드캐스트 받기

### Manifest-declared receivers (정적 리시버)

Oreo(API Level 26) 이상은 몇몇 브로드캐스트를 제외하고는 정적 리시버를 사용할 수 없다. 대신에 scheduled jobs를 사용해야한다.

1. manifest에 리시버 선언.

```xml
        <receiver android:name=".MyBroadcastReceiver"  android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
                <action android:name="android.intent.action.INPUT_METHOD_CHANGED" />
            </intent-filter>
        </receiver>
```

인텐트 필터는 리시버가 구독할 브로드캐스트의 action을 구체화한다.

2. BroadcastReceiver를 상속하고 onReceive를 구현한다.
```kotlin
        private const val TAG = "MyBroadcastReceiver"
        
        class MyBroadcastReceiver : BroadcastReceiver() {
        
            override fun onReceive(context: Context, intent: Intent) {
                StringBuilder().apply {
                    append("Action: ${intent.action}\n")
                    append("URI: ${intent.toUri(Intent.URI_INTENT_SCHEME)}\n")
                    toString().also { log ->
                        Log.d(TAG, log)
                        Toast.makeText(context, log, Toast.LENGTH_LONG).show()
                    }
                }
            }
        }
```
시스템 패키지 매니저가 앱이 설치될 때 리시버도 함께 등록한다. 해당 리시버는 분리된 entry point가 될 수도 있다. 즉, 앱이 실행중이 아니더라도 브로드캐스트를 받았을 때 앱이 시작될 수도 있다는 말이다.

시스템은 리시버가 각각의 브로드캐스트를 받을 때마다 새로운 브로드캐스트리시버를 만들어낸다. 해당 객체는 onReceive가 호출되는 동안만 살아있게 된다. 한 번 코드에서 return이 되면 시스템은 더 이상 해당 컴포넌트가 활성화되어있지 않다고 처리한다.

### Context-registered receivers (동적 리시버)

1. BroadcastReceiver 인스턴스를 생성한다.
```kotlin
        val br: BroadcastReceiver = MyBroadcastReceiver()
```
2. IntentFilter를 생성하고 리시버에 등록한다.
```kotlin
        val filter = IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION).apply {
            addAction(Intent.ACTION_AIRPLANE_MODE_CHANGED)
        }
        registerReceiver(br, filter)
```

local broadcast를 등록하고 싶다면, LocalBroadcastManager.registerReceiver(BroadcastReceiver, IntentFilter)를 사용한다.

동적 리시버는 등록한 Context가 유효한 동안만 브로드캐스트를 수신한다.

3. 브로드캐스트 수신을 중단하고 싶다면, unregisterReceiver(android.content.BroadcastReceiver)를 호출한다. Context가 유효하지 않거나, 더 이상 리시버가 필요하지 않을 때 확실하게 등록을 해지한다. 리시버의 등록과 해제할 때 신경을 써줘야한다. onCreate에 등록했다면 onDestroy에 해지하고, onResume에 등록했다면 onPause에 해지해야한다. onSaveInstanceState(Bundle)에서는 해지를 해서는 안된다. 액티비티가 종료될 때 해당 콜백은 불리지 않기 때문이다.

### 상태

브로드캐스트리시버의 상태는 리시버를 가지고 있는 프로세스의 상태에 영향을 받는다. 프로세스가 리시버를 실행시키고 onReceive가 실행중이면 이는 포그라운드 프로세스로 처리된다. 따라서 메모리 부족 상황에서도 리시버는 살아있게 된다. 그러나 onReceive가 종료되면 브로드캐스트리시버는 비활성화된다. 정적 리시버는 onReceive 후에 우선순위가 낮아져 프로세스가 메모리로부터 삭제될 수 있다.

따라서 브로드캐스트리시버에서는 오랜 시간동안 실행되는 백그라운드 쓰레드를 실행시켜서는 안된다. onReceive 후에 시스템이 프로세스를 없앨 수 있으므로 산출된 쓰레드도 삭제될 수 있다. 이를 피하기 위해서 goSync()를 사용하여 백그라운드 쓰레드에서 조금 더 오랜시간동안 브로드캐스트를 처리하거나 JobScheduler를 사용하여 JobService를 스케쥴해야한다. goSync()는 메인쓰레드에서의 과도한 로드를 방지하기 위해 다른 쓰레드에서 작업을 수행하도록 한다.
```kotlin
    private const val TAG = "MyBroadcastReceiver"
    
    class MyBroadcastReceiver : BroadcastReceiver() {
    
        override fun onReceive(context: Context, intent: Intent) {
            val pendingResult: PendingResult = goAsync()
            val asyncTask = Task(pendingResult, intent)
            asyncTask.execute()
        }
    
        private class Task(
                private val pendingResult: PendingResult,
                private val intent: Intent
        ) : AsyncTask<String, Int, String>() {
    
            override fun doInBackground(vararg params: String?): String {
                val sb = StringBuilder()
                sb.append("Action: ${intent.action}\n")
                sb.append("URI: ${intent.toUri(Intent.URI_INTENT_SCHEME)}\n")
                return toString().also { log ->
                    Log.d(TAG, log)
                }
            }
    
            override fun onPostExecute(result: String?) {
                super.onPostExecute(result)
                // Must call finish() so the BroadcastReceiver can be recycled.
                pendingResult.finish()
            }
        }
    }
```
## 브로드캐스트 보내기

안드로이드는 브로드캐스트를 보내는 세 가지 방법을 제공한다.

- sendOrderedBroadcast(Intent, String)

    일반 브로드캐스트는 완전히 Async로 작동하기 때문에 다수의 Receiver를 신경쓰지 않아도 된다. OrderedBroadcast도 Async이지만 IntentFilter의 android:priority 중요도에 따라 수신 순서가 정해지고 한 번에 하나씩 전달된다. 먼저 Broadcast를 수신한 Receiver의 onReceive()가 return 되어야 다음 Receiver에게 Broadcast가 전달된다. OrderedBroadcast를 수신한 Receiver에서는 Abort flag와 Result code, data, extras를 Set/Get 할 수 있다.

- sendBroadcast(Intent)

    가장 일반적인 방법으로 순서없이 모든 리시버에게 브로드캐스트를 보낸다. 보다 효율적이지만 이는 리시버가 다른 리시버의 결과를 읽거나, 브로드캐스트에서 수신한 데이터를 전파하거나 브로드캐스트를 중단할 수 없음을 의미한다.

- LocalBroadcastManager.sendBroadcast

    같은 앱 내에서만 브로드캐스트를 수신할 수 있도록 브로드캐스트를 보낸다. 커뮤니케이션 비용이 줄어들기 때문에 매우 효율적이다.
```kotlin
    Intent().also { intent ->
        intent.setAction("com.example.broadcast.MY_NOTIFICATION")
        intent.putExtra("data", "Notice me senpai!")
        sendBroadcast(intent)
    }
```
## Restricting broadcasts with permissions

퍼미션을 사용하면 특정 퍼미션을 보유한 앱으로만 브로드캐스트를 제한할 수 있다. sender와 receiver 모두에 제한을 걸 수 있다.

### Sending with permissions

sendBroadcast(Intent, String), sendOrderedBroadcast(Intent, String, BroadcastReceiver, Handler, int, String, Bundle)를 호출할 때, 퍼미션 파라미터를 설정할 수 있다. 앱은 오직 manifest에 해당 퍼미션이 요청된 후에야 브로드캐스트를 수신할 수 있다.
```kotlin
    sendBroadcast(Intent("com.example.NOTIFY"), Manifest.permission.SEND_SMS)
```
```xml
    <uses-permission android:name="android.permission.SEND_SMS"/>
```
### Receiving with permissions

registerReceiver(BroadcastReceiver, IntentFilter, String, Handler) 또는 <receiver> 태그에서 브로드캐스트리시버를 등록할 때, 특정 퍼미션 파라미터를 설정하면, 오직 <uses-permission> 태그를 manifest에서 선언한 브로드캐스터만이 리시버에 인텐트를 보낼 수 있다.
```xml
    <receiver android:name=".MyBroadcastReceiver"
              android:permission="android.permission.SEND_SMS">
        <intent-filter>
            <action android:name="android.intent.action.AIRPLANE_MODE"/>
        </intent-filter>
    </receiver>
```
```kotlin
    var filter = IntentFilter(Intent.ACTION_AIRPLANE_MODE_CHANGED)
    registerReceiver(receiver, filter, Manifest.permission.SEND_SMS, null )
```
```xml
    <uses-permission android:name="android.permission.SEND_SMS"/>
```
## Security considerations and best practices

- 외부 컴포넌트에 데이터를 제공할 필요가 없다면 LocalBroadcastManager 이용하기.
- 많은 앱들이 같은 브로드캐스트를 수신하도록 등록되어 있다면, 한꺼번에 많은 앱이 런칭될 위험이 있다. 이를 방지하기 위해 동적 리시버를 사용하는 것이 권장된다.
- 암시적 인텐트로 민감한 정보를 브로드캐스트하지 않는다. 브로드캐스트를 받기 위해 등록된 어떠한 앱에서도 정보는 읽힐 수 있다. 방지하기 위한 세 가지 방법은 다음과 같다.
    - 브로드캐스트를 보낼 때 퍼미션을 설정한다.
    - Android 4.0 이상이면, setPackage(String)로 package를 설정한다. 시스템은 오직 매칭되는 패키에만 브로드캐스트를 보낸다.
    - LocalBroadcastManager로 로컬 브로드캐스트를 보낸다.
- 리시버를 등록할 때, 어떤 앱이든지 악성 브로드캐스트를 보낼 수 있다. 방지하기 위한 세 가지 방법은 다음과 같다.
    - 브로드캐스트리시버를 등록할 때 퍼미션을 설정한다.
    - 정적 리시버에는 android:exported를 false로 설정한다. 외부 앱으로부터 브로드캐스트를 받지 않도록 설정한다.
    - LocalBroadcastManager로 로컬 브로드캐스트만 받도록 제한한다.
- 브로드캐스트 action의 namespace는 global이다. action 이름과 namespace의 스트링이 본인의 것만임을 확실히 해야한다. 그렇지 않으면 다른 앱과 충돌할 수 있다.
- onReceive(Context, Intent)는 메인쓰레드에서 실행되므로 실행과 return이 빨라야한다. 긴 작업이 필요하다면 다음 두 가지 방법을 사용한다.
    - goAsync()를 리시버의 onReceive()에서 실행하고 BroadcastReceiver.PendingResult를 백그라운드 쓰레드로 전달한다. 이는 브로드캐스트를 onReceive return 후에도 활성 상태로 유지시켜준다. 그러나 이러한 접근을 하더라도 시스템은 작업이 빨리 끝나기를 기대한다 (10초 이내). 이는 작업을 다른 쓰레드로 옮겨서 메인 쓰레드에서의 안좋은 영향을 방지한다.
    - JobScheduler로 job을 스케쥴링한다.
- 브로드캐스트리시버에서 액티비티를 시작하지 않도록 한다. 이는 UX에 큰 방해요소이다. 특히 리시버가 하나 이상이라면 notification을 띄우는 것을 고려한다.
