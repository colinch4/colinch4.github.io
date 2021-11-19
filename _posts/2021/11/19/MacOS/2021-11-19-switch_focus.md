---
layout: post
title: "[MacOS] Switch Focus"
description: " "
date: 2021-11-19
tags: [MacOS]
comments: true
share: true
---

# Switch Focus <small>(MacOS)</small>
> 듀얼모니터 유저를 위한 마우스 없이 마우스 자유자재로 다루는 법

1. 마우스 옮기기
2. 포커스 바꾸기

![wo-mouse](https://user-images.githubusercontent.com/48475824/74578733-ac927b80-4fd9-11ea-92cd-475d70ba3806.png)  

듀얼 모니터를 사용하게 되면 mouse focus를 위해 부득불 마우스를 사용해야만 한다.  
키보드에서 마우스로 손을 움직이는 동작은 번거롭게만 느껴진다.   

이러한 번거로움을 줄이기 위해 키보드로 마우스 커서 이동 및 포커스를 다루는 법을 알아보았다. 



## 마우스 커서 옮기기
> 다중 모니터간에 키보드로 마우스 커서 옮기는 법
 
모니터 간에 마우스 커서를 옮기는 법을 알아보자.  
이를 가능하게 하기 위해 필요한 Application은 [Maxim Leyzerovich](http://round.is/about/) 가 만든 **CatchMouse** 이다.  

### How to set up
1. Download the Application  
   * [CatchMouse App 이 위치한 Github 페이지](https://github.com/round/CatchMouse)로 접속
   * Download the ZIP file  
      <img width="395" alt="download-zip" src="https://user-images.githubusercontent.com/48475824/74579299-f6c92c00-4fdc-11ea-9ea7-62a36619ddf0.png">
1. Unzip it
1. Open it
     * Open 시에 MacOS로 인해 App 사용이 block 되어 있다면  
        <img width="414" alt="verify-catchMouse" src="https://user-images.githubusercontent.com/48475824/74579480-33495780-4fde-11ea-8f25-16b8e9643690.png">  
        > Apple menu > System Preferences > Security & Privacy  

        에서 CatchMouse 를 Allow 시켜준다.  
        ![allow-it](https://user-images.githubusercontent.com/48475824/74579620-2d07ab00-4fdf-11ea-98de-66640ba7b125.png)  
        > Accessibility 
        
        에서 CatchMouse를 선택해준다.  
        ![allow-access](https://user-images.githubusercontent.com/48475824/74579660-912a6f00-4fdf-11ea-9d3e-73fbd82de722.png)

1. CatchMouse Set up
     * 모니터는 최대 4개까지 사용 가능하다.  
       <img width="403" alt="CatchMout-setup" src="https://user-images.githubusercontent.com/48475824/74579392-7d7e0900-4fdd-11ea-98d9-f1a9f021d685.png">  
    원하는 Shorcut key 입력.  
    다른 단축키와 겹치지 않도록 주의하여 설정할 것!

여기까지는 마우스 커서를 단순히 Monitor 1 에서 다른 Monitor 2 또는 Monitor 3으로 옮기기만 가능하다.   
포커스를 바꾸기 위해서는 그 다음 세팅을 해주어야 한다.  

![multi-monitor](https://user-images.githubusercontent.com/48475824/74579026-4ad31100-4fdb-11ea-8dbe-a717de45fea2.png)



## 마우스 포커스 바꾸기  
> 다중 모니터간에 키보드로 마우스 포커스 바꾸는 법  

키보드를 이용해 마우스 포커스를 바꾸는 법을 알아보자.  
이를 가능하게 하기 위해 다운로드 해야 할 것은 **Karabiner-Elements** 이다.

<img width="200" alt="Karabiner-Elements" src="https://user-images.githubusercontent.com/48475824/74579866-5a555880-4fe1-11ea-867b-3ba35042c10a.png">


### How to set up
1. Download it
   * 간단히 brew 를 통해 install  
    <code>brew cask install karabiner-elements</code>  
      ```bash
      // 다운로드 성공
      installer: Package name is Karabiner-Elements 12.9.0
      installer: Installing at base path /
      installer: The install was successful.
      🍺  karabiner-elements was successfully installed!
      ```
1. Open it  
   > Apple menu > System Preferences > Security & Privacy > Input Monitoring  

   karabiner_grabber 와 karabiner_observer 두개를 선택해 준다.  
   ![allow-karabiner](https://user-images.githubusercontent.com/48475824/74579944-2d557580-4fe2-11ea-8caf-0bda5b9f7f8e.png)
2. Karabiner-elements Set up  
   단축키 세팅해주기  
   ![setup-shortcut](https://user-images.githubusercontent.com/48475824/74579966-5d9d1400-4fe2-11ea-84f7-81a8ce81d4da.png)  
   * button1 : 마우스 왼쪽 클릭
   * button2 : 마우스 오른쪽 클릭


이로서 세팅이 모두 끝났다 :)  
이제 대부분의 시간을 키보드와 함께하면 된다!
