---
layout: post
title: "setoneditoractionlistener 예제"
description: " "
date: 2023-09-25
tags: [setoneditoractionlistener]
comments: true
share: true
---

```java
EditText editText = findViewById(R.id.edit_text);
editText.setOnEditorActionListener(new TextView.OnEditorActionListener() {
    @Override
    public boolean onEditorAction(TextView textView, int actionId, KeyEvent keyEvent) {
        if (actionId == EditorInfo.IME_ACTION_DONE) {
            // 사용자가 키보드의 완료(또는 동일) 버튼을 눌렀을 때 실행되는 코드
            // 엔터 키 등을 사용하는 다른 경우도 처리할 수 있습니다.
            
            String userInput = editText.getText().toString();
            // 입력된 텍스트를 가져와 처리하는 로직을 여기에 작성하세요.
            
            return true; // 이벤트를 소모하고 종료합니다.
        }
        return false; // 이벤트를 계속해서 처리하도록 합니다.
    }
});
```

위의 코드는 `EditText` 위젯에 `setOnEditorActionListener`를 설정하는 방법을 보여줍니다. 사용자가 키보드의 완료(또는 동일) 버튼을 누르면 `onEditorAction` 메서드가 호출되고 입력된 텍스트를 처리하는 로직을 작성할 수 있습니다.

이 예제를 활용하여 해당 이벤트를 사용하는 경우에 맞게 코드를 작성하면 됩니다. 예를 들어, 사용자가 텍스트 입력을 완료하면 검색 기능을 수행하거나, 다음 입력 필드로 이동하는 등의 동작을 구현할 수 있습니다.