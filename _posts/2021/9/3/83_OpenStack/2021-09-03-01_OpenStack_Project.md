---
layout: post
title: "[OpenStack] OpenStack Project"
description: " "
date: 2021-09-03
tags: [개발]
comments: true
share: true
---

## # OpenStack Project

## 0. 용어

- 언더클라우드

  > 오픈스택의 컴포넌트를 오버클라우드에 배포하고 관리하는 관리용 클라우드

- 오버클라우드

  > 오픈스택의 서비스가 구동되는 노드 집합
  >
  > 워크로드 클라우드
  >
  > 생성된 가상 머신은 오버클라우드에서 구동

- 테넌트 

  > 항목 그룹(사용자, 이미지, 인스턴스, 네트워크 등)

- Flavor

  > 인스턴스에 연결된 하드웨어. RAM, CPU 및 디스크 포함

- 스택

  > 템플릿에서 빌드하는 인스턴스 그룹
  >
  > 템플릿 파일은 JSON 형식
  >
  > 스택 및 템플릿 파일은 Heat 오케스트레이션 서비스에 사용

- Director

  > 오픈스택 환경을 설치하고 관리하는 툴 => UnderCloud - OverCloud를 설치 및 설정

- Ephemeral disk

  > 인스턴스에서 사용되는 임시 디스크



## 1. Horizon (Dashboard)

- 웹을 통해 사용자나 관리자가 오픈스택의 자원과 서비스를 이용할 수 있도록 사용자 인터페이스를 제공하는 서비스
- 컨트롤러 노드에 설치하고, 아파치 웹 서버 사용



## 2. Nova (Compute)

### 2-1. 특징

- 컴퓨트 노드에 설치되어 CPU, MEM, 네트워크, 스토리지를 이용해 가상 머신 서비스를 제공
- 하이퍼바이저와 상호 작용하는 드라이버를 이용해 하이퍼바이저 외부에서 가상 머신을 제어하는 방식
- 다수의 컴퓨트 노드에 독립적으로 설치
- 컴퓨트 노드와 컨트롤러 노드 간의 통신은 AMQP 프로토콜을 사용하는 큐 이용(비동기식)



### 2-2. 컴포넌트

![](https://github.com/dh77hd/Note/blob/master/83_OpenStack/image/01_nova.PNG?raw=true)

- Nova-api
- Nova-scheduler
- Nova-compute
- Nova-conductor



### 2-3. 로그

> /var/log/nova/nova-api.log
>
> /var/log/nova/nova-cert.log
>
> /var/log/nova/nova-compute.log
>
> /var/log/nova/nova-conductor.log
>
> /var/log/nova/nova-consoleauth.log
>
> /var/log/nova/nova-manage.log
>
> /var/log/nova/nova-novncproxy.log
>
> /var/log/nova/nova-scheduler.log



### 2-4. 명령어





## 3. Neutron (Network) 

### 3-1. 특징

- 클라우드 환경의 네트워크 연결을 정의하고 네트워킹 기능 제공
- Nova가 관리하는 가상 머신이 사용하는 네트워크, 스위치, 서브넷 및 라우터를 포함하여 가상 네트워크 인프라의 생성과 관리를 처리하는 서비스
- 가상 방화벽, VPN, 로드밸런서 서비스도 지원
- 가상 머신 내부의 가상 스위치에 플러그인되어 Nova와 요청을 주고 받음



### 3-2. 컴포넌트

![](https://github.com/dh77hd/Note/blob/master/83_OpenStack/image/01_neutron.PNG?raw=true)

- Neutron-server
- Neutron-dhcp-agent
- Neutron-L3 agent
- Neutron-L2 agent



### 3-3. 네트워크 타입

- 테넌트 네트워크

  > 가상 머신들이 연결되는 가상화된 네트워크
  >
  > 사용자 포털을 통해 사용자가 프로젝트별로 네트워크를 생성하여 직접 관리할 수 있는 네트워크
  >
  > 프로젝트별로 테넌트 네트워크 여러 개 생성 가능

- 프로바이더 네트워크

  > 외뷔와 연결 고리 역할을 하는 네트워크
  >
  > 가상 머신이 외부와 연결하기 위해서는 프로바이더 네트워크를 경유



### 3-4. 로그

> /var/log/neutron/dhcp-agent.log
> /var/log/neutron/l3-agent.log
> /var/log/neutron/metadata-agent.log
> /var/log/neutron/metering-agent.log
> /var/log/neutron/openvswitch-agent.log
> /var/log/neutron/ovs-cleanup.log
> /var/log/neutron/server.log



### 3-5. 명령어





## 4. Cinder (Block Storage)

### 4-1. 특징

- 가상 머신에 블록 스토리지를 제공하는 서비스
- 내부 스토리지 장착 또는 외부 스토리지 서버 공유 방식(iSCSI, NFS)



### 4-2. 컴포넌트

![](https://github.com/dh77hd/Note/blob/master/83_OpenStack/image/01_cinder.PNG?raw=true)

- cinder-api

  > Cinder를 통해 스토리지 서비스를 제공하는 API 인터페이스

- cinder-scheduler

  > 볼륨 서비스 요청의 실행과 전달을 관리

- cinder-volume

  > 백엔드의 블록 스토리지 장치를 관리하는 기능을 수행

- cinder-backup

  > Cinder가 제공하는 블록 스토리지를 오픈스택의 Swift로 백업할 수 있는 기능 제공



### 4-3. 로그



### 4-4. 명령어





## 5. Swift (Object Storage)

### 5-1. 특징

- 비정형 객체를 저장하는 저장 공간 서비스
- 파일 또는 폴더와 같은 컨테이너 형태 지원
- HTTP 기반으로 RESTful API를 통해 서비스 제공
- 주로 백업과 가상 머신 이미지, 사진, 비디오 등 아카이브 데이터의 저장 공간으로 이용
- 스케일아웃 아키텍처로 구성
- 3 Copy 기반



### 5-2. 컴포넌트

- swift-proxy-server
- swift-object-server
- swift-account-server
- swift-container-server



### 5-3. 로그



### 5-4. 명령어



## 6. Keystone (Identity)

### 6-1. 특징

- 오픈스택의 인증 서비스를 제공
- Keystone이 중단되면 오픈스택의 어떤 서비스에도 접근할 수 없음
- 인증 외에도 사용자 관리, 보안 그룹 관리, REST 기반 API 를 제공하는 각종 서비스의 Endpoint URL을 관리하는 기능 제공
- 사용자별로 PKI 기반의 키 페어가 생성되어 사용자 정보 데이터베이스에 저장

### 6-2. 용어

- 프로젝트 : 사용자 및 사용자가 소유한 리소스의 컬렉션
- 사용자 : OpenStack을 사용하는 사람 또는 클라우드 사용자
- 역할 : OpenStack 서비스의 특정 작업을 수행하는 사용자 권한 정의 / admin 및 _ member_ 의 두 가지 역할 제공
- 자격 증명 : 사용자를 인증하기 위해 Keystone에 필요한 인증 데이터 / 사용자 이름, 암호, 프로젝트 이름, Keystone 엔드포인트, 지역 이름이 포함
- 지역 : OSP 배포를 논리적으로 나타내는 데 사용
- 그룹 : 특정 도메인 내에 있는 사용자 컬렉션
- 도메인 : 단일 ID 도메인 내에 정의할 수 있는 프로젝트 및 사용자의 컬렉션 / 도메인은 개인, 회사 또는 클라우드 운영자에 매핑 가능

### 6-3. 컴포넌트



### 6-4. 로그



### 6-5. 명령어

**프로젝트 생성** 

```
openstack project create --description [discription] --domain [domain_name] --project [project_name]
```

**그룹 생성**

```
openstack group create [group_name]
```

**프로젝트 사용자 추가**

~~~
openstack role add --project [project_name] --user [user_name] [role]
~~~

**사용자 생성**

```
openstack user create --project [project_name] --password-prompt [user_name]
```



## 7. Glance (Image)

### 7-1. 특징

- 오픈스택이 제공하는 이미지 관리 서비스
- 



### 7-2. 컴포넌트

![](https://github.com/dh77hd/Note/blob/master/83_OpenStack/image/01_glance.PNG?raw=true)

- 
- 



### 7-3. 로그



### 7-4. 명령어

 

## 8. Ceilometer (Telemetry)

### 8-1. 특징

- 클라우드에서 발생하는 각종 정보를 측정하여 사용량 조회, 과금, 사용 내역 조회 등을 사용자에게 제공하는 서비스
- NoSQL 데이터베이스가 필요하며, 오픈스택에서는 MongoDB 사용하고 컨트롤러 노드에 설치



## 9. Heat (Orchestration)

### 9-1. 특징

- 텍스트 파일 형태로 제공되는 HOT라는 템플릿 파일을 기반으로 여러 유형의 복합 클라우드 응용 프로그램을 배포할 수 있는 통합 관리 엔진
- 가상 머신의 자원 할당, 설정 변경, 부하에 따른 가상 머신 오토스케일링 등을 자동화 할 수 있는 도구 제공
- YAML로 작성



## 8. Ironic (Bare Metal)

- PXE나 IPMI를 이용해 베어메탈을 네트워크로 부팅시켜 컴퓨트 서비스를 제공할 수 있도록 지원
- Nova에 통합



## 9. Trove (DB as a Service)

- 관계현 데이터베이스와 비관계형 데이터베이스를 서비스로 제공하는 배포 엔진



## 10. Sahara(Elastic Map Reduce)

- Hadoop 클러스터를 간단한 방법으로 사용자에게 제공한느 서비스
- Hadoop 클러스터의 구성 기능과 클러스터 노드 추가 및 제거 기능 제공



## 11. Designate (DNS)

- DNS의 기능을 서비스로 제공하기 위한 프로젝트



## 12. Octavia (LB)



## 13. Magnum (Container Orchestration Engine)

- Docker와 K8S를 포함한 운영체제 이미지를 제공하기 위해 Heat를 사용하고, 그 운영체제 이미지를 가상 머신 또는 베어메탈 서버에서 실행하여 컨테이너 서비스 제공



## . Zun (Container)













## 1. 용어

* 



## 2. 

  source keystone_<user> : 사용자 권한 얻기
  openstack help project show : 
  openstack project show <project_name> : 사용자의 현재 프로젝트에 관한 정보
  openstack user show <user_name> : 계정 세부 정보
  openstack flavor list : flavor 리스트 정보 나열
  openstack flavor show <flavor_name> : flavor 세부 정보 표시
  openstack image list : 사용 가능한 모든 이미지 나열
  openstack server list : 사용 가능한 모든 인스턴스
  openstack server show <instance> : instance 세부 정보 표시

  openstack help <command> <command-action> : 사용 가능한 명령 목록

  neutron net-list : 사용 가능한 네트워크 나열
  nova list : 사용 가능한 인스턴스

  openstack server create --image <image> --flavor <flavor> : 인스턴스 생성

  openstack project create --description <description> --domain <domain> --enable <project_name> : 프로젝트 생성

  openstack quota show <project_name> : 프로젝트 할당량 표시
  openstack quota set --core <> --ram <> .. <project_name> : 할당량 수정

  openstack status : openstack 서비스 상태 확인
  openstack-service status : 실행 중인 각 openstack 서비스 상태 나열

  openstack console url show network-instance : network-instance 의 콘솔 URL
  ethtool -i <interface> : interface 네트워크 드라이버 확인

### 2-2. Image

  openstack image create --disk-format <format> --file <file path> <image_name> : image 생성
  openstack image set --protected --min-disk <disk_volume> <image_name> : image 수정

### 2-3. OVS

* br-int : 통합 브릿지. VLAN 태깅 및 언태깅
* br-ex : 외부 브리지. 외부 트래픽 라우팅
* qg : 라우터를 게이트웨이에 연결
* qr : 라우터를 통합 브리지 br-int에 연결
* qvo : 통합 브리지에 연결
* qvb : qvo를 통해 방화벽 브리지를 br-int에 연결
* qbr : OpenStack 보안 그룹을 제공하는 Linux 브리지

  ovs-vsctl 명령을 사용하여 Open vSwitch 브리지 관리 / 브리지 및 포트 생성, 확인, 삭제 / 외부 SDN 컨트롤러 연결 가능 /
  ovs-vsctl show : 
  ovs-vsctl add-br <bridge> : bridge 생성
  ovs-vsctl del-br <bridge> : bridge 삭제
  ovs-vsctl list-br : 모든 bridge 나열
  ovs-vsctl add-port <bridge> <port> : bridge에 port 추가
  ovs-vsctl del-port <bridge> <port> :
  ovs-vsctl list-ifaces <bridge> : bridge의 모든 인터페이스 이름 나열

  ovs-ofctl 명령은 openflow 스위치를 모니터링하고 관리하는 도구 /
  ovs-ofctl show : openflow DB
  ovs-ofctl dump-ports-desc : 포트 상태 검색
  ovs-ofctl dump-flows : flow 항목 표시

  ovs-dpctl show : 스위치 데이터 경로 표시

### 2-4. OSP Network

    #### 수신 패킷 흐름

1. 인바운드 패킷이 물리적 시스템의 eth0으로 이동합니다.
2. 패킷이 eth0에서 br-ex 브리지로 전송됩니다.
3. 그런 다음 패킷이 통합 브리지 br-int로 전송됩니다.
4. 패킷이 br-int에 도착하면 br-int 브리지 내에서 OVS 흐름 규칙에 따라 수정됩니다. OVS 흐름 규칙은 패킷에 VLAN 태그를 추가하고 qvo로 전달합니다.
5. qvo에서 패킷을 수락하면 VLAN 태그를 제거하고 qvb로 전달합니다.
6. qvb에서 패킷을 수신하고 보안 그룹 규칙을 적용합니다.
7. 트래픽의 진행을 방해하는 규칙이 없으면 패킷이 인스턴스에 도착합니다.

  

openstack network create <network_name> --shared(external) : network 생성

openstack subnet create --subnet-range <range> --dns-nameserver <dns> --network <network_name> <subnet_name> : network 생성 후, subnet 생성

###  2-5. Swap Disk

parted /dev/vdc print : /dev/vdc에서 스왑디스크 사용 가능한지 확인
parted -s /dev/vdc mklabel msdos mkpart primary linux-swap 1M 1G : /dev/vdc 에서 새 파티션 생성
mkswap /dev/vdc1 : 스왑 파티션으로 /dev/vdc1 구성
swapon /dev/vdc1 : 스왑 파티션 활성

parted /dev/vdb print : /dev/vdb에서 임시디스크 사용 가능한지 확인
parted -s /dev/vdb mklabel msdos mkpart primary xfs 1M 2G : /dev/vdb 에 새 파티션 생성
mkfs.xfs /dev/vdb1 : /dev/vdb1 파티션에 XFS 파일 시스템 생성
mkdir /temporary
mount -t xfs /dev/vdb1 /temporary : /temporary 디렉터리에 /dev/vdb1 파티션 마운트

[Volume]
openstack server add volume <instance_name> <volume_name> : 볼륨을 인스턴스에 연결
a
[Object]
  (1) 컨테이너
    - 오브젝트 스토리지의 칸에 해당
    - 컨테이너 사용시, 오브젝트 구성 가능
    - 중첩 X, 계정 내에서 무제한 생성 가능
  (2) 오브젝트
    - 저장된 데이터
    - 파일의 확장 특성(xattrs)에 저장되는 메타데이터와 함께 이진 파일로 저장되는
    - 텍스트, 동영상, 이미지, 이메일, 가상시스템 이미지 ...
  (3) 의사 폴더
    - 컨테이너 내에 생성 가능, 중첩 가능

openstack container create <container_name> : 컨테이너 생성
openstack container list :
openstack container delete <container_name> :
openstack object create <container_name> <folder_name>/<file> : 파일 오브젝트 생성
openstack object save 
