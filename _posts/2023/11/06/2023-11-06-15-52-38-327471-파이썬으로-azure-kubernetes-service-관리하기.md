---
layout: post
title: "파이썬으로 Azure Kubernetes Service 관리하기"
description: " "
date: 2023-11-06
tags: [python]
comments: true
share: true
---

Azure Kubernetes Service (AKS)는 Azure에서 호스팅되는 관리형 Kubernetes 서비스입니다. 이 서비스를 사용하면 쉽게 Kubernetes 클러스터를 프로비저닝, 관리 및 확장할 수 있습니다. 이번 블로그 포스트에서는 파이썬으로 AKS를 관리하는 방법을 알아보겠습니다.

## AKS 모듈 설치하기

AKS를 관리하기 위해서는 `azure-identity`, `azure-mgmt-containerservice`, `kubernetes-azure-python` 모듈이 필요합니다. 다음 명령을 사용하여 모듈을 설치하세요:

```python
pip install azure-identity azure-mgmt-containerservice kubernetes-azure-python
```

## AKS 클러스터 생성하기

AKS 클러스터를 생성하기 위해서는 Azure Active Directory 인증을 사용해야 합니다. 다음은 파이썬 코드를 사용하여 AKS 클러스터를 생성하는 예제입니다:

```python
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.containerservice.models import ManagedCluster

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
credential = DefaultAzureCredential()

client = ContainerServiceClient(credential, subscription_id)
location = "eastus"
resource_group_name = "myresourcegroup"
cluster_name = "myakscluster"

cluster_params = ManagedCluster(
    location=location,
    dns_prefix=cluster_name,
    kubernetes_version="1.19.3",
    agent_pool_profiles=[
        {
            "name": "agentpool",
            "count": 3,
            "vm_size": "Standard_D2_v2"
        }
    ]
)

client.managed_clusters.begin_create_or_update(resource_group_name, cluster_name, cluster_params)
```

## AKS 클러스터 관리하기

AKS 클러스터를 생성한 후에는 다양한 작업을 수행할 수 있습니다. 예를 들어, 클러스터 정보 조회, 노드 확장 또는 축소, 파드 배포 등을 할 수 있습니다. 다음은 AKS 클러스터를 관리하는 예제 코드입니다:

```python
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
credential = DefaultAzureCredential()

client = ContainerServiceClient(credential, subscription_id)
resource_group_name = "myresourcegroup"
cluster_name = "myakscluster"

# 클러스터 정보 조회
cluster = client.managed_clusters.get(resource_group_name, cluster_name)
print(f"Cluster Name: {cluster.name}")
print(f"Kubernetes Version: {cluster.kubernetes_version}")
print(f"Provisioning State: {cluster.provisioning_state}")

# 노드 확장 또는 축소
client.managed_clusters.begin_update(resource_group_name, cluster_name, {"agentPoolProfiles": [
    {
        "name": "agentpool",
        "count": 4  # 노드 개수 증가
    }
]})

# 파드 배포
client.managed_clusters.begin_create_or_update(resource_group_name, cluster_name, {"addonProfiles": {
    "http_application_routing": {"enabled": True}
}})
```

## 마치며

이번 포스트에서는 파이썬을 사용하여 Azure Kubernetes Service (AKS)를 관리하는 방법에 대해 알아보았습니다. AKS 클러스터를 생성하고 관리하는 방법을 익히면 Kubernetes 기반 애플리케이션을 쉽게 배포하고 조작할 수 있습니다. Azure Python SDK의 다른 기능과 함께 AKS를 사용하는 방법을 더 알아보기 위해 [공식 문서](https://docs.microsoft.com/python/api/overview/azure/kubernetes-service?view=azure-python)를 참조해주세요.

`#Azure` `#Kubernetes`