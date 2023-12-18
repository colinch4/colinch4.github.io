---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 파일 업로드 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

파일을 업로드할 때 사용자에게 실시간으로 진행 상황을 보여주는 것은 매우 중요합니다. 이를 위해 Flutter에서는 `LinearProgressIndicator` 위젯을 사용하여 파일 업로드 진행률을 실시간으로 표시할 수 있습니다.

## 1. LinearProgressIndicator 위젯 추가

먼저, 파일 업로드가 진행되는 동안에 표시할 `LinearProgressIndicator` 위젯을 화면에 추가합니다.

```dart
LinearProgressIndicator(
  value: _uploadProgress,
  minHeight: 10,
),
```

여기서 `_uploadProgress`는 파일 업로드 진행률을 나타내는 변수입니다.

## 2. 파일 업로드 진행률 갱신

파일 업로드 중에는, 진행률이 업데이트 될 때마다 `_uploadProgress` 값을 변경하여 `LinearProgressIndicator`를 갱신해야 합니다. 파일 업로드 과정에서 진행률을 감시하고 갱신하는 코드는 다음과 같을 수 있습니다.

```dart
StorageUploadTask uploadTask = storageRef.putFile(file);
uploadTask.events.listen((event) {
  setState(() {
    _uploadProgress = event.snapshot.bytesTransferred / event.snapshot.totalByteCount;
  });
});
```

## 3. 완료 처리

파일 업로드가 완료되면, `LinearProgressIndicator`를 숨기거나 완료 메시지를 표시할 수 있습니다.

```dart
if (_uploadProgress == 1.0) {
  Scaffold.of(context).showSnackBar(SnackBar(content: Text('Upload complete')));
}
```

이제, 파일 업로드 중에 사용자에게 실시간 진행률을 보여주기 위해 `LinearProgressIndicator`를 구현했습니다.

## 마무리

이제 파일 업로드 진행률을 표시하는데 `LinearProgressIndicator` 위젯을 성공적으로 활용할 수 있습니다. 이를 통해 사용자는 파일 업로드가 얼마나 더 걸릴지에 대한 시각적인 피드백을 받을 수 있게 됩니다.

---
위젯의 자세한 사용법은 [공식 Flutter 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)를 참고하시기 바랍니다.