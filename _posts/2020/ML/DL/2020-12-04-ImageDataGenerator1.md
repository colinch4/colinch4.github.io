---
layout: post
title: "[DL] ImageDataGenerator의 사용 - 1"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# ImageDataGenerator1의 사용(개와 고양이)

> TF2.X 에서 이미지 증식을 위해서 사용하는 ImageDataGenerator를 간단히 알아보고 image를 확인해 본다.



## 사용 Library

> 사용하는 library들이다.

```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
```



## 데이터셋

> train data와 validation date를 정의한다.

```python
train_dir      = './data/cat_dog_full/train'
validation_dir = './data/cat_dog_full/validation'

# 전체 데이터가 25,000장 (고양이 : 12,500, 개 : 12,500)
# 댕댕이 이미지 train      : 7,000장
# 댕댕이 이미지 validation : 3,000장
# 댕댕이 이미지 test       : 2,500장
```



## ImageDataGenerator

> ImageDataGenerator 에 대해서 간단히 알아본다. 데이터 증식(augmentation)은 아래에서 진행한다.

* generator 생성

```python
train_datagen = ImageDataGenerator(rescale=1/255) 
validation_datagen=ImageDataGenerator(rescale=1/255)

train_generator = train_datagen.flow_from_directory(train_dir,
                                                    classes=['cats', 'dogs'],
                                                    batch_size = 20,
                                                    target_size = (150, 150)
                                                    class_mode='binary')

validation_generator = validation_datagen.flow_from_directory(validataion_dir,
                                                              classes=['cats', 'dogs'],
                                                              batch_size = 20,
                                                              target_size = (150, 150),
                                                              class_mode = 'binary')
```



* x_data, t_data 추출 : `batch_size=20`이므로 20장씩 랜덤으로 무한번 추출된다. 따라서 `break`를 걸어 데이터를 확인한다.

```python
for x_data, t_data in train_generator:
    print(x_data.shape)  # (20, 150, 150, 3)
    print(type(x_data))  # <class 'numpy.ndarray'>
    print(t_data)        # [1. 0. 0. 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 0. 0.]
    # 0 : 고양이,  1 : 댕댕이
```



* 사진 확인  : `enumerate`를 사용해 확인해 본다. (x_data에 대한 enumerate는 조금 다르다. 맨 앞의 값을 가져오지 않는다.)

```python
fig = plt.figure(figsize=(10, 10))
axs = []

for x_data, t_data in train_generator:
    for idx, img enumerate(x_data):
        axs.append(fig.add_subplot(5,4,idx+1))
        plt.imshow(axs[idx])
    break
```

![image-20201107144516477](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201107144516477.png?raw=true)



## data augmentation (데이터 증식)

> `ImageDataGenerator`를 사용해 데이터 증식하는 법을 알아본다. 여기서는 `.flow_from_directory`가 아닌 `.flow`를 사용해 알아본다.

* Library

```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
```



* image 확인 : `image.load_img` 을 사용한다.

```python
img = image.load_img('./data/cat_dog_small/train/cats/cat.3.jpg', target_size=(150, 150)) print(type(img)) # <class 'PIL.Image.Image'>

plt.imshow(img)
plt.show()
```

![image-20201107165006652](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201107165006652.png?raw=true)

* 이미지 array로 바꿔 한번 더 확인 및 차원 증가시키기 

```python
x = image.img_to_array(img)
print('x_shape : ',x.shape)  # x_shape :  (150, 150, 3)
print('x_type : ',type(x))   # x_type :  <class 'numpy.ndarray'>
print(x.dtype)               # float32
# plt.imshow(x) : error 발생, 원인 : imshow는 0-1 float 또는 0-255 int 값을 input값으로 받음
plt.imshow(np.unit8(x))
plt.show()

x = x.reshape((1,) + x.shape)
```

![image-20201107165745422](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201107165745422.png?raw=true)

* ImageDataGenerator 및 data 증식

```python
datagen = ImageDataGenerator(rotation_range = 90,
                             width_shift_range=0.4,
                             height_shift_range=0.4,
                             vertical_flip =True,
                             horizontal_flip =True)

idx = 0
fig = plt.figure(figsize=(10, 10))
axs = []
for batch in datage.flow(x , batch_size=1): # 여기서 batch는 x가 됨
    axs.append(flg.add_subplot(5, 4, idx+1))
    axs[idx].imshow(image.array_to_img(batch[0]))
    idx += 1
    if idx%20 == 0:
        break
fig.tight_layout()
plt.show()
```

![image-20201107172032692](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201107172032692.png?raw=true)