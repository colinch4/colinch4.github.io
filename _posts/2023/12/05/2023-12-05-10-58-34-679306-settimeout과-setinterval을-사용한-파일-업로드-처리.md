---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 파일 업로드 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

파일 업로드는 웹 개발에서 자주 사용되는 기능 중 하나입니다. 사용자가 웹 페이지를 통해 파일을 선택하면, 선택한 파일을 서버로 전송하는 과정을 처리해야 합니다. 이때, 파일 업로드가 크거나 인터넷 속도가 느리면 업로드 과정에서 시간이 오래 걸릴 수 있습니다. 

이러한 업로드 과정에서 사용자에게 진행 상황을 알려주기 위해, setTimeout과 setInterval 함수를 사용할 수 있습니다. setTimeout 함수는 일정 시간이 지난 후 한 번만 실행되는 함수이고, setInterval 함수는 일정 시간 간격으로 반복해서 실행되는 함수입니다.

아래 예제 코드는 파일 업로드 과정에서 setTimeout과 setInterval을 사용하여 업로드 진행 상황을 표시하는 예시입니다.

```javascript
// 파일 업로드 함수
function uploadFile(file) {
  // 파일 업로드 시작
  console.log('업로드 시작:', file.name);
  
  var progress = 0;
  var timerId = setInterval(function() {
    // 업로드 진행 상황 표시
    console.log('업로드 진행 중:', progress + '%');
    progress += 10;
    
    if (progress >= 100) {
      // 업로드 완료
      console.log('업로드 완료:', file.name);
      clearInterval(timerId); // setInterval 함수 중지
    }
  }, 1000);
  
  // 파일 업로드 완료 후 처리
  setTimeout(function() {
    console.log('업로드 후처리:', file.name);
  }, 5000);
}

// 파일 선택 이벤트 핸들러
function handleFileSelect(event) {
  var files = event.target.files;
  
  for (var i = 0; i < files.length; i++) {
    uploadFile(files[i]);
  }
}

// 파일 선택 이벤트 리스너 등록
var fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', handleFileSelect);
```

위 코드에서 `uploadFile` 함수는 파일을 업로드하는 함수입니다. 업로드 시작 시 '업로드 시작: 파일이름'을 출력하고, setInterval 함수를 사용하여 업로드 진행 상황을 표시합니다. progress 변수는 업로드 진행 상황을 나타내는 변수로, 10씩 증가시킵니다. progress가 100이 되면 '업로드 완료: 파일이름'을 출력하고 setInterval 함수를 중지합니다. 

setTimeout 함수는 파일 업로드 완료 후 5초 뒤에 '업로드 후처리: 파일이름'을 출력합니다.

마지막으로, 파일 선택 이벤트 핸들러(`handleFileSelect`)는 사용자가 파일을 선택하면 업로드를 수행하기 위해 `uploadFile` 함수를 호출합니다.

위 예제 코드를 실행하면 파일 업로드 과정에서 파일 이름과 업로드 진행 상황, 업로드 완료, 업로드 후처리 메시지가 출력됩니다.

---

## 참고 자료
- [MDN web docs - setTimeout](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN web docs - setInterval](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)