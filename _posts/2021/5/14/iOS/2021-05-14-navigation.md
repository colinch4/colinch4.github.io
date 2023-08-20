---
layout: post
title: "[iOS] NavigationBar"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---

## NavigationBar 설정

**네비게이션바 숨기기**   
![f1](https://user-images.githubusercontent.com/45002556/108619393-ebb6a080-7467-11eb-92d0-fa3bdbcd4161.png)

**네비게이션바 색깔**
1. **tintColor**     
    navigation items와 bar button items에 적용되는 색깔
    ![f2](https://user-images.githubusercontent.com/45002556/108619394-ed806400-7467-11eb-9eeb-8316ae042e29.png)
    ![f3](https://user-images.githubusercontent.com/45002556/108619395-ef4a2780-7467-11eb-9443-73635813b3e7.png)

    
2. **barTintColor**    
    NavigationBar background로 적용되는 색깔. isTranslucent를 false로 설정하지 않으면 기본적으로 반투명이다
    ![f4](https://user-images.githubusercontent.com/45002556/108619412-0be65f80-7468-11eb-8863-c6daf2408680.png)
    ![f5](https://user-images.githubusercontent.com/45002556/108619413-0d178c80-7468-11eb-9c25-c1539fb0f3da.png)    

    navigationbar와 view 모두 gray로 설정을 했지만 색이 다르다는걸 알 수 있다

    따라서 isTransLucent를 설정해야 한다    
![f6](https://user-images.githubusercontent.com/45002556/108619414-0db02300-7468-11eb-9481-a24407052d6d.png)
![f7](https://user-images.githubusercontent.com/45002556/108619433-346e5980-7468-11eb-88ff-9931c9ef10f6.png)

3. **backgroundColor**
    backgroundColor는    
    ![f8](https://user-images.githubusercontent.com/45002556/108619445-45b76600-7468-11eb-8438-458c51535db9.png)
    
    여기서 사용되는 backgroundColor와 같다. view의 backgroundColor
    ![f9](https://user-images.githubusercontent.com/45002556/108619450-4a7c1a00-7468-11eb-936d-97161079c321.png)
    ![f10](https://user-images.githubusercontent.com/45002556/108619452-4bad4700-7468-11eb-80c9-4451b8b31f3c.png)

    - backgroundColor

    ![f11](https://user-images.githubusercontent.com/45002556/108619454-4c45dd80-7468-11eb-8e20-7ae3326a411b.png)
    - barTintColor
