---
layout: post
title: "[안드로이드] InputMethodManager 란"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---


화면에 나오는 soft 키보드를 제어하는 클래스.  

생성자로 객체 생성이 불가능하며, getSystemService 메소드로 가져와야 함.  


```
//InputMethodManager 객체 가져오기

InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
```


화면에 보일때는 showSoftInput() 메소드를, 숨길 때는 hideSoftInputFromWindow() 메소드를 사용한다.  

```
// 키보드 보이기

imm.showSoftInput(editText, InputMethodManager.SHOW_IMPLICIT);

// 키보드 숨기기

imm.hideSoftInputFromWindow(getCurrentFocus().getWindowToken(),         // edittext.getWindowToken() 도 가능

InputMethodManager.HIDE_NOT_ALWAYS);

```


## showSoftInput() 로도 화면에 키보드가 보이지 않는 경우  

1. EditText 객체에 포커스를 주고 showSoftInput() 메소드를 실행하기.  


```
editText.requestFocus();
imm.showSoftInput(editText, InputMethodManager.SHOW_IMPLICIT);

```

2. toggleSoftInput() 메소드 사용. 키보드가 없으면 보이게하고 보이면 사라지게함  

```

imm.toggleSoftInput(InputMethodManager.SHOW_FORCED,0);

```


3. 잠시 딜레이를 가지고 실행하도록 한다. 30ms정도?

```
editText.postDelayed(new Runnable()
        {
            @Override
            public void run()
            {
                et_searchBar.requestFocus();
                imm.showSoftInput(et_searchBar, 0);
            }
        }, 30);

```

