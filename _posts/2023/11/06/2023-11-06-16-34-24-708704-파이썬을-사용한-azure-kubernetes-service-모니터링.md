---
layout: post
title: "파이썬을 사용한 Azure Kubernetes Service 모니터링"
description: " "
date: 2023-11-06
tags: [Azure, Kubernetes]
comments: true
share: true
---

Azure Kubernetes Service(AKS)는 Azure에서 제공하는 Kubernetes 관리 서비스로, 애플리케이션 컨테이너를 손쉽게 배포하고 관리할 수 있습니다. 이번 글에서는 파이썬을 사용하여 AKS 클러스터의 상태를 모니터링하는 방법에 대해 알아보겠습니다.

## 필요한 패키지 설치

**Kubernetes 클라이언트 라이브러리 설치하기**
```python
pip install kubernetes
```

## AKS 클러스터와 연결하기

```python
from kubernetes import client, config

# Azure 관리자 인증 정보로 AKS 클러스터에 연결
config.load_kube_config()

# CoreV1Api 인스턴스 생성
api_instance = client.CoreV1Api()
```

## 클러스터의 노드 목록 가져오기

```python
def get_node_list():
    # API를 통해 노드 정보 가져오기
    nodes = api_instance.list_node().items

    # 각 노드에 대한 정보 출력
    for node in nodes:
        node_name = node.metadata.name
        node_status = node.status.conditions[-1].status
        
        print(f"Node Name: {node_name}")
        print(f"Node Status: {node_status}")
```

## 파드 목록 가져오기

```python
def get_pod_list():
    # API를 통해 파드 정보 가져오기
    pods = api_instance.list_pod_for_all_namespaces().items

    # 각 파드에 대한 정보 출력
    for pod in pods:
        pod_name = pod.metadata.name
        pod_namespace = pod.metadata.namespace
        pod_status = pod.status.phase
        
        print(f"Pod Name: {pod_name}")
        print(f"Namespace: {pod_namespace}")
        print(f"Pod Status: {pod_status}")
```

## 메트릭 가져오기

```python
def get_cluster_metrics():
    # API를 통해 메트릭 정보 가져오기
    metrics_api = client.MetricsV1beta1Api()
    metrics = metrics_api.list_node_metrics().items

    # 각 메트릭에 대한 정보 출력
    for metric in metrics:
        node_name = metric.metadata.name
        cpu_usage = metric.usage["cpu"]
        memory_usage = metric.usage["memory"]
        
        print(f"Node Name: {node_name}")
        print(f"CPU Usage: {cpu_usage}")
        print(f"Memory Usage: {memory_usage}")
```

## 실행하기

```python
if __name__ == "__main__":
    get_node_list()
    get_pod_list()
    get_cluster_metrics()
```

위의 예제 코드는 파이썬으로 Azure Kubernetes Service(이하 AKS)를 모니터링하는 방법을 보여줍니다. 해당 코드를 실행하면 AKS 클러스터의 노드 목록, 파드 목록, 그리고 클러스터의 메트릭을 가져올 수 있습니다.

이러한 모니터링 기능을 사용하여 AKS 클러스터의 성능 관련 문제를 감지하고 신속하게 대응할 수 있습니다. AKS와 파이썬을 함께 사용하여 효율적인 클러스터 관리를 할 수 있도록 노력해 보세요!

**관련 참고 자료:**
- [Azure Kubernetes Service 문서](https://docs.microsoft.com/azure/aks/)
- [kubernetes-client 라이브러리 문서](https://github.com/kubernetes-client/python)
- [AKS 모니터링 가이드 문서](https://docs.microsoft.com/azure/azure-monitor/containers/container-insights-aks)

#Azure #Kubernetes #파이썬