---
layout: post
title: "[DL] ImageDataGenerator의 사용 - 3"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# ImageDataGenerator3의 사용(개와 고양이)

 > TF2.X 에서 이미지 증식을 사용해 개와 고양이 문제를 CNN 을 통해 확인해 본다.



## 사용 Library

> 사용하는 library들이다.

```python
import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.optimizers import Adam
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

> train 및 validation directory를 가져와 ImageDataGenerator를 생성한다.

```python
train_datagen = ImageDataGenerator(rescale=1/255,
                                   horizontal_flip=True,
                                   ratation_range = 30,
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   shear_range = 0.2,  # 층밀림의 강도
                                   zoom_range = 0.2)

validation_datagen = ImageDataGenerator(rescale=1/255)


train_generator = train_datagen.flow_from_directory(train_dir,
                                                    classes=['cats', 'dogs'],
                                                    batch_size=20,
                                                    target_size=(150, 150),
                                                    class_mode = 'binary')


validation_generator = train_datagen.flow_from_directory(validation_dir,
                                                        classes= ['cats', 'dogs'],
                                                        batch_size =20,
                                                        target_size=(150,150),
                                                        class_mode = 'binary')
                                          class_mode = 'binary')
```



## 모델 생성 및 학습

> CNN 구조를 만들고 학습시킨다.

```python
model = Sequential()

model.add(Conv2D(filters = 32, kernel_size=(3, 3) ,activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(filters = 64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(filters = 128, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(filters = 256, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(filters = 256, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())

model.add(Dropout(0.5))

model.add(Dense(512, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer=Adam(learning_rate=1e-4),
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_generator, steps_per_epoch=700, epochs=100, validation_data=validation_generator, validation_steps=300)
```



## 결과

> validation accuracy를 알아 본다.

```python
Once deleted, variables cannot be recovered. Proceed (y/[n])? y
Found 14000 images belonging to 2 classes.
Found 6000 images belonging to 2 classes.
Epoch 1/100
700/700 [==============================] - 137s 196ms/step - loss: 0.6516 - accuracy: 0.6048 - val_loss: 0.5806 - val_accuracy: 0.6882
Epoch 2/100
700/700 [==============================] - 120s 171ms/step - loss: 0.5747 - accuracy: 0.6971 - val_loss: 0.5463 - val_accuracy: 0.7183
Epoch 3/100
700/700 [==============================] - 120s 171ms/step - loss: 0.5386 - accuracy: 0.7296 - val_loss: 0.5202 - val_accuracy: 0.7395
Epoch 4/100
700/700 [==============================] - 121s 172ms/step - loss: 0.5162 - accuracy: 0.7448 - val_loss: 0.4975 - val_accuracy: 0.7607
Epoch 5/100
700/700 [==============================] - 121s 173ms/step - loss: 0.4936 - accuracy: 0.7621 - val_loss: 0.4422 - val_accuracy: 0.7962
Epoch 6/100
700/700 [==============================] - 120s 171ms/step - loss: 0.4648 - accuracy: 0.7762 - val_loss: 0.4266 - val_accuracy: 0.8055
Epoch 7/100
700/700 [==============================] - 120s 171ms/step - loss: 0.4510 - accuracy: 0.7854 - val_loss: 0.4085 - val_accuracy: 0.8128
Epoch 8/100
700/700 [==============================] - 120s 172ms/step - loss: 0.4380 - accuracy: 0.7902 - val_loss: 0.3970 - val_accuracy: 0.8257
Epoch 9/100
700/700 [==============================] - 120s 172ms/step - loss: 0.4264 - accuracy: 0.8062 - val_loss: 0.3815 - val_accuracy: 0.8268
Epoch 10/100
700/700 [==============================] - 120s 172ms/step - loss: 0.4150 - accuracy: 0.8079 - val_loss: 0.3803 - val_accuracy: 0.8283
Epoch 11/100
700/700 [==============================] - 120s 171ms/step - loss: 0.4009 - accuracy: 0.8209 - val_loss: 0.3668 - val_accuracy: 0.8388
Epoch 12/100
700/700 [==============================] - 121s 173ms/step - loss: 0.3835 - accuracy: 0.8261 - val_loss: 0.4248 - val_accuracy: 0.8065
Epoch 13/100
700/700 [==============================] - 121s 173ms/step - loss: 0.3731 - accuracy: 0.8339 - val_loss: 0.3682 - val_accuracy: 0.8432
Epoch 14/100
700/700 [==============================] - 120s 171ms/step - loss: 0.3661 - accuracy: 0.8357 - val_loss: 0.3269 - val_accuracy: 0.8562
Epoch 15/100
700/700 [==============================] - 117s 167ms/step - loss: 0.3562 - accuracy: 0.8405 - val_loss: 0.3903 - val_accuracy: 0.8275
Epoch 16/100
700/700 [==============================] - 117s 167ms/step - loss: 0.3487 - accuracy: 0.8481 - val_loss: 0.3428 - val_accuracy: 0.8523
Epoch 17/100
700/700 [==============================] - 118s 168ms/step - loss: 0.3360 - accuracy: 0.8536 - val_loss: 0.3131 - val_accuracy: 0.8632
Epoch 18/100
700/700 [==============================] - 117s 167ms/step - loss: 0.3297 - accuracy: 0.8553 - val_loss: 0.3217 - val_accuracy: 0.8580
Epoch 19/100
700/700 [==============================] - 116s 166ms/step - loss: 0.3226 - accuracy: 0.8596 - val_loss: 0.3052 - val_accuracy: 0.8652
Epoch 20/100
700/700 [==============================] - 115s 164ms/step - loss: 0.3073 - accuracy: 0.8621 - val_loss: 0.2836 - val_accuracy: 0.8773
Epoch 21/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2965 - accuracy: 0.8728 - val_loss: 0.2838 - val_accuracy: 0.8778
Epoch 22/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2996 - accuracy: 0.8688 - val_loss: 0.2891 - val_accuracy: 0.8718
Epoch 23/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2895 - accuracy: 0.8753 - val_loss: 0.2621 - val_accuracy: 0.8853
Epoch 24/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2801 - accuracy: 0.8789 - val_loss: 0.3216 - val_accuracy: 0.8607
Epoch 25/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2740 - accuracy: 0.8841 - val_loss: 0.2734 - val_accuracy: 0.8802
Epoch 26/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2726 - accuracy: 0.8846 - val_loss: 0.2455 - val_accuracy: 0.8938
Epoch 27/100
700/700 [==============================] - 114s 163ms/step - loss: 0.2652 - accuracy: 0.8869 - val_loss: 0.2573 - val_accuracy: 0.8890
Epoch 28/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2594 - accuracy: 0.8913 - val_loss: 0.2812 - val_accuracy: 0.8857
Epoch 29/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2526 - accuracy: 0.8916 - val_loss: 0.2414 - val_accuracy: 0.8982
Epoch 30/100
700/700 [==============================] - 117s 168ms/step - loss: 0.2456 - accuracy: 0.8946 - val_loss: 0.2344 - val_accuracy: 0.9010
Epoch 31/100
700/700 [==============================] - 119s 169ms/step - loss: 0.2385 - accuracy: 0.9014 - val_loss: 0.2583 - val_accuracy: 0.8867
Epoch 32/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2366 - accuracy: 0.8976 - val_loss: 0.2349 - val_accuracy: 0.9013
Epoch 33/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2401 - accuracy: 0.8990 - val_loss: 0.2274 - val_accuracy: 0.9037
Epoch 34/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2265 - accuracy: 0.9036 - val_loss: 0.2223 - val_accuracy: 0.9053
Epoch 35/100
700/700 [==============================] - 116s 165ms/step - loss: 0.2234 - accuracy: 0.9067 - val_loss: 0.2163 - val_accuracy: 0.9030
Epoch 36/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2159 - accuracy: 0.9109 - val_loss: 0.2375 - val_accuracy: 0.8968
Epoch 37/100
700/700 [==============================] - 115s 164ms/step - loss: 0.2084 - accuracy: 0.9117 - val_loss: 0.2109 - val_accuracy: 0.9095
Epoch 38/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2108 - accuracy: 0.9111 - val_loss: 0.2371 - val_accuracy: 0.8962
Epoch 39/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2115 - accuracy: 0.9121 - val_loss: 0.2025 - val_accuracy: 0.9130
Epoch 40/100
700/700 [==============================] - 116s 165ms/step - loss: 0.2009 - accuracy: 0.9144 - val_loss: 0.1986 - val_accuracy: 0.9145
Epoch 41/100
700/700 [==============================] - 115s 165ms/step - loss: 0.2025 - accuracy: 0.9136 - val_loss: 0.1966 - val_accuracy: 0.9162
Epoch 42/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1986 - accuracy: 0.9170 - val_loss: 0.2189 - val_accuracy: 0.9042
Epoch 43/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1924 - accuracy: 0.9208 - val_loss: 0.2323 - val_accuracy: 0.9080
Epoch 44/100
700/700 [==============================] - 114s 163ms/step - loss: 0.1931 - accuracy: 0.9199 - val_loss: 0.1886 - val_accuracy: 0.9202
Epoch 45/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1891 - accuracy: 0.9212 - val_loss: 0.1992 - val_accuracy: 0.9137
Epoch 46/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1836 - accuracy: 0.9239 - val_loss: 0.1839 - val_accuracy: 0.9222
Epoch 47/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1857 - accuracy: 0.9244 - val_loss: 0.1902 - val_accuracy: 0.9217
Epoch 48/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1804 - accuracy: 0.9269 - val_loss: 0.1993 - val_accuracy: 0.9203
Epoch 49/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1729 - accuracy: 0.9299 - val_loss: 0.2044 - val_accuracy: 0.9157
Epoch 50/100
700/700 [==============================] - 114s 163ms/step - loss: 0.1781 - accuracy: 0.9274 - val_loss: 0.1898 - val_accuracy: 0.9200
Epoch 51/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1711 - accuracy: 0.9288 - val_loss: 0.1872 - val_accuracy: 0.9178
Epoch 52/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1755 - accuracy: 0.9281 - val_loss: 0.1845 - val_accuracy: 0.9227
Epoch 53/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1648 - accuracy: 0.9334 - val_loss: 0.1694 - val_accuracy: 0.9290
Epoch 54/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1636 - accuracy: 0.9328 - val_loss: 0.1878 - val_accuracy: 0.9180
Epoch 55/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1645 - accuracy: 0.9302 - val_loss: 0.1703 - val_accuracy: 0.9273
Epoch 56/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1636 - accuracy: 0.9322 - val_loss: 0.1693 - val_accuracy: 0.9297
Epoch 57/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1597 - accuracy: 0.9334 - val_loss: 0.2046 - val_accuracy: 0.9108
Epoch 58/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1603 - accuracy: 0.9356 - val_loss: 0.2020 - val_accuracy: 0.9153
Epoch 59/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1614 - accuracy: 0.9351 - val_loss: 0.2159 - val_accuracy: 0.9048
Epoch 60/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1540 - accuracy: 0.9359 - val_loss: 0.1779 - val_accuracy: 0.9307
Epoch 61/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1522 - accuracy: 0.9386 - val_loss: 0.2063 - val_accuracy: 0.9153
Epoch 62/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1536 - accuracy: 0.9370 - val_loss: 0.1816 - val_accuracy: 0.9233
Epoch 63/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1530 - accuracy: 0.9374 - val_loss: 0.1705 - val_accuracy: 0.9293
Epoch 64/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1472 - accuracy: 0.9401 - val_loss: 0.2004 - val_accuracy: 0.9170
Epoch 65/100
700/700 [==============================] - 118s 169ms/step - loss: 0.1475 - accuracy: 0.9391 - val_loss: 0.1641 - val_accuracy: 0.9313
Epoch 66/100
700/700 [==============================] - 119s 170ms/step - loss: 0.1425 - accuracy: 0.9424 - val_loss: 0.1568 - val_accuracy: 0.9337
Epoch 67/100
700/700 [==============================] - 115s 165ms/step - loss: 0.1443 - accuracy: 0.9419 - val_loss: 0.1604 - val_accuracy: 0.9372
Epoch 68/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1412 - accuracy: 0.9438 - val_loss: 0.2134 - val_accuracy: 0.9197
Epoch 69/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1402 - accuracy: 0.9429 - val_loss: 0.1629 - val_accuracy: 0.9332
Epoch 70/100
700/700 [==============================] - 115s 164ms/step - loss: 0.1332 - accuracy: 0.9449 - val_loss: 0.1569 - val_accuracy: 0.9363
Epoch 71/100
700/700 [==============================] - 116s 166ms/step - loss: 0.1386 - accuracy: 0.9456 - val_loss: 0.1553 - val_accuracy: 0.9333
Epoch 72/100
700/700 [==============================] - 116s 166ms/step - loss: 0.1369 - accuracy: 0.9431 - val_loss: 0.1762 - val_accuracy: 0.9277
Epoch 73/100
700/700 [==============================] - 117s 167ms/step - loss: 0.1360 - accuracy: 0.9434 - val_loss: 0.1760 - val_accuracy: 0.9278
Epoch 74/100
700/700 [==============================] - 117s 167ms/step - loss: 0.1315 - accuracy: 0.9477 - val_loss: 0.1652 - val_accuracy: 0.9315
Epoch 75/100
700/700 [==============================] - 116s 166ms/step - loss: 0.1351 - accuracy: 0.9441 - val_loss: 0.1909 - val_accuracy: 0.9268
Epoch 76/100
700/700 [==============================] - 116s 166ms/step - loss: 0.1346 - accuracy: 0.9467 - val_loss: 0.1539 - val_accuracy: 0.9347
Epoch 77/100
700/700 [==============================] - 116s 166ms/step - loss: 0.1313 - accuracy: 0.9476 - val_loss: 0.1718 - val_accuracy: 0.9307
Epoch 78/100
700/700 [==============================] - 117s 167ms/step - loss: 0.1278 - accuracy: 0.9491 - val_loss: 0.1727 - val_accuracy: 0.9278
Epoch 79/100
700/700 [==============================] - 117s 167ms/step - loss: 0.1228 - accuracy: 0.9502 - val_loss: 0.1553 - val_accuracy: 0.9382
Epoch 80/100
700/700 [==============================] - 117s 167ms/step - loss: 0.1268 - accuracy: 0.9480 - val_loss: 0.1572 - val_accuracy: 0.9395
Epoch 81/100
700/700 [==============================] - 116s 166ms/step - loss: 0.1314 - accuracy: 0.9468 - val_loss: 0.1560 - val_accuracy: 0.9368
Epoch 82/100
700/700 [==============================] - 118s 168ms/step - loss: 0.1228 - accuracy: 0.9510 - val_loss: 0.1612 - val_accuracy: 0.9367
Epoch 83/100
700/700 [==============================] - 116s 165ms/step - loss: 0.1226 - accuracy: 0.9496 - val_loss: 0.1939 - val_accuracy: 0.9242
Epoch 84/100
700/700 [==============================] - 117s 167ms/step - loss: 0.1225 - accuracy: 0.9494 - val_loss: 0.1494 - val_accuracy: 0.9438
Epoch 85/100
700/700 [==============================] - 112s 160ms/step - loss: 0.1258 - accuracy: 0.9504 - val_loss: 0.1532 - val_accuracy: 0.9393
Epoch 86/100
700/700 [==============================] - 112s 161ms/step - loss: 0.1215 - accuracy: 0.9521 - val_loss: 0.1536 - val_accuracy: 0.9405
Epoch 87/100
700/700 [==============================] - 113s 161ms/step - loss: 0.1179 - accuracy: 0.9525 - val_loss: 0.1642 - val_accuracy: 0.9335
Epoch 88/100
700/700 [==============================] - 112s 160ms/step - loss: 0.1185 - accuracy: 0.9524 - val_loss: 0.1491 - val_accuracy: 0.9400
Epoch 89/100
700/700 [==============================] - 113s 161ms/step - loss: 0.1125 - accuracy: 0.9567 - val_loss: 0.1619 - val_accuracy: 0.9400
Epoch 90/100
700/700 [==============================] - 113s 161ms/step - loss: 0.1197 - accuracy: 0.9521 - val_loss: 0.1614 - val_accuracy: 0.9382
Epoch 91/100
700/700 [==============================] - 112s 161ms/step - loss: 0.1197 - accuracy: 0.9530 - val_loss: 0.1662 - val_accuracy: 0.9367
Epoch 92/100
700/700 [==============================] - 112s 160ms/step - loss: 0.1106 - accuracy: 0.9550 - val_loss: 0.1533 - val_accuracy: 0.9403
Epoch 93/100
700/700 [==============================] - 113s 161ms/step - loss: 0.1082 - accuracy: 0.9571 - val_loss: 0.1608 - val_accuracy: 0.9380
Epoch 94/100
  1/700 [..............................] - ETA: 0s - loss: 0.0896 - accuracy: 0.9500
```