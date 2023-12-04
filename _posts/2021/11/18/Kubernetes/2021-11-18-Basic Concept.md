---
layout: post
title: "[Kubernetes] Basic Concept"
description: " "
date: 2021-11-18
tags: [개발]
comments: true
share: true
---

Kubernetes
---------
#### UseFul WebSite

* [What is Kubernetes?][a]

[a]:https://subicura.com/2019/05/19/kubernetes-basic-1.html

* [CNCF][b]

[b]:https://landscape.cncf.io/

#### Desired state

<img src="https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/desired-state.png" width="50%">

* current state
* imperative 命令
* declarative 宣言

~~~~~
$ docker run # 명령
$ kubectl create # 상태 생성
~~~~~

#### Kubernetes Object

* **Pod**

<img src="https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/pod.png" width="50%">


> * 쿠버네티스에서 배포할 수 있는 가장 작은 단위
> * 한 개 이상의 컨테이너와 스토리지, 네트워크 속성을 가짐
> * Pod에 속한 컨테이너는 스토리지와 네트워크를 공유하고 서로 localhost로 접근


* **ReplicaSet**

<img src="https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/replicaset.png" width="50%">

> * Pod을 여러 개(한 개 이상) 복제하여 관리하는 오브젝트
> * Pod을 생성하고 개수를 유지하려면 반드시 ReplicaSet을 사용
> * ReplicaSet은 복제할 개수, 개수를 체크할 라벨 선택자, 생성할 Pod의 설정값(템플릿)등을 가짐

* **Service**
> 네트워크와 관련된 오브젝트

* **Volume**
> 저장소와 관련된 오브젝트입니다.

* **Object Spec - YAML**

[Ref][k]

[k]:https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/kubernetes-objects/
~~~~~yaml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
~~~~~
+ apiVersion - 이 오브젝트를 생성하기 위해 사용하고 있는 쿠버네티스 API 버전이 어떤 것인지
+ kind - 어떤 종류의 오브젝트를 생성하고자 하는지
+ metadata - 이름 문자열, UID, 그리고 선택적인 네임스페이스를 포함하여 오브젝트를 유일하게 구분지어 줄 데이터
+ spec - 오브젝트에 대해 어떤 상태를 의도하는지

#### 쿠버네티스 배포방식

> 쿠버네티스는 애플리케이션을 배포하기 위해 원하는 상태(desired state)를 다양한 오브젝트(object)에 라벨Label을 붙여 정의(yaml)하고 API 서버에 전달하는 방식을 사용


### 쿠버네티스 아키텍처
