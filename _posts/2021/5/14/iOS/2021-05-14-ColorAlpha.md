---
layout: post
title: "[iOS] View의 Alpha값 변경"
description: " "
date: 2021-05-14
tags: [ios]
comments: true
share: true
---

## View의 Alpha값 변경    
View의 background를 지정하고 alpha 값을 수정하면 sub view들의 alpha 값 또한 영향을 받는다.   
따라서 다음 코드와 같이 view의 색과 alpha 값을 지정하면 sub view들에게 영향을 주지 않는다.    

### withAlphaComponent(alpha 값)
```swift        
view.backgroundColor = UIColor.black.withAlphaComponent(0.75)
```
