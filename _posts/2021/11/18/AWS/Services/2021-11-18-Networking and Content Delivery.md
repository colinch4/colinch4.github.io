---
layout: post
title: "[AWS] services - Networking 과 Content Delivery"
description: " "
date: 2021-11-18
tags: [AWS]
comments: true
share: true
---

Amazon Virtual Private Cloud (VPC)
---
+ AWS 리소스를 고객이 정의한 가상 네트워크에서 실행할 수 있는 서비스
+ 이 가상 네트워크는 AWS의 확장 가능한 인프라를 사용한다는 이점과 함께 고객의 자체 데이터 센터에서 운영하는 기존 네트워크와 매우 유사

>
> ### Virtual Private Cloud(VPC) 
> 사용자의 AWS 계정 전용 가상 네트워크입니다.
>
> ### 서브넷
> VPC의 IP 주소 범위입니다.
>
> ### 라우팅 테이블
> 네트워크 트래픽을 전달할 위치를 결정하는 데 사용하는 라우팅이라는 이름의 규칙 집합입니다.
>
> ### 인터넷 게이트웨이
> VPC의 리소스와 인터넷 간의 통신을 활성화하기 위해 VPC에 연결하는 게이트웨이입니다.
>
> ### VPC 엔드포인트
> 인터넷 게이트웨이, NAT 디바이스, VPN 연결 또는 AWS Direct Connect 연결 없이도 PrivateLink로 구동하는 지원되는 AWS 서비스 및 VPC 엔드포인트 서비스에 비공개로 연결할 수 있게 합니다. VPC의 인스턴스는 서비스의 리소스와 통신하는 데 퍼블릭 IP 주소를 필요로 하지 않습니다. VPC와 기타 서비스 간의 트래픽은 Amazon 네트워크를 벗어나지 않습니다. 자세한 내용은 VPC 엔드포인트 및 VPC 엔드포인트 서비스(AWS PrivateLink)를 참조하십시오.

AWS CloudFront
---
> + .html, .css, .js 및 이미지 파일과 같은 정적 및 동적 웹 콘텐츠를 사용자에게 더 빨리 배포하도록 지원하는 웹 서비스
> + CloudFront는 엣지 로케이션이라고 하는 데이터 센터의 전 세계 네트워크를 통해 콘텐츠를 제공
> + 사용자가 요청하면 지연 시간이 가장 낮은 엣지 로케이션으로 라우팅되므로 콘텐츠 전송 성능이 뛰어남
>
>![cloudfront](https://docs.aws.amazon.com/ko_kr/AmazonCloudFront/latest/DeveloperGuide/images/how-you-configure-cf.png)
>
> ## 원본 액세스 ID(OAI)를 이용한 Amazon S3 액세스 제한
> + 원본 액세스 ID(OAI)라는 특수 CloudFront 사용자를 만들어 배포와 연결합니다.
> + CloudFront에서 OAI를 사용하여 버킷의 파일을 액세스해 사용자에게 제공할 수 있도록 S3 버킷 권한을 구성합니다. 사용자가 S3 버킷에 대한 직접 URL을 사용하여 파일에 액세스할 수 없도록 해야 합니다.
> + 이 단계를 수행하면 사용자가 S3 버킷에서 직접 액세스하지 않고 CloudFront를 통해서만 파일에 액세스할 수 있습니다.

AWS Direct Connect
---
표준 1기가비트 또는 10기가비트 이더넷 광섬유 케이블을 통해 내부 네트워크를 AWS Direct Connect 위치에 연결
케이블의 한쪽 끝은 사용자의 라우터에 연결되고 다른 쪽 끝은 AWS Direct Connect 라우터에 연결됩니다.
이 연결을 사용하면 AWS 클라우드 및 Amazon Virtual Private Cloud로 직접적인 가상 인터페이스를 만들어 사용자의 네트워크 경로에서 인터넷 서비스 공급자를 우회할 수 있습니다.

AWS Direct Connect는 IPv4 및 IPv6 통신 프로토콜을 모두 지원합니다.
퍼블릭 AWS 서비스에서 제공하는 IPv6 주소는 AWS Direct Connect 퍼블릭 가상 인터페이스를 통해 액세스할 수 있습니다.


Elastic Load Balancing
---
#### Application Load Balancer, Network Load Balancer 및 Classic Load Balancer.
[Comparison](https://blueyikim.tistory.com/category/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%20%EC%BB%B4%ED%93%A8%ED%8C%85/%EC%95%84%EB%A7%88%EC%A1%B4%28AWS%29)
+ 로드 밸런서 이점
로드 밸런서는 워크로드를 가상 서버와 같은 다수의 컴퓨팅 리소스로 분산합니다.
로드 밸런서를 사용하면 애플리케이션의 가용성과 내결함성이 높아집니다.
애플리케이션에 대한 요청의 전체적인 흐름을 방해하지 않고
필요에 따라 로드 밸런서에서 컴퓨팅 리소스를 추가 및 제거할 수 있습니다.


> + 관련 서비스
Elastic Load Balancing은 다음 서비스를 통해 애플리케이션의 가용성 및 확장성을 개선합니다.

> + Amazon EC2 — 클라우드에서 애플리케이션을 실행하는 가상 서버입니다. 로드 밸런서를 구성하여 EC2 인스턴스에 트래픽을 라우팅할 수 있습니다.
> + Amazon EC2 Auto Scaling — 인스턴스에 장애가 발생하더라도 원하는 수의 인스턴스를 실행하고 인스턴스의 수요가 변경되면 자동으로 인스턴스 수를 늘리거나 줄일 수 있게 해 줍니다. Elastic Load Balancing,과 함께 Auto Scaling을 활성화하는 경우, Auto Scaling이 시작한 인스턴스는 자동으로 로드 밸런서에 등록되고 Auto Scaling이 종료하는 인스턴스는 자동으로 로드 밸런서에서 등록 취소됩니다.
> + AWS Certificate Manager — HTTPS 리스너를 생성할 때 ACM에서 제공한 인증서를 지정할 수 있습니다. 로드 밸런서는 인증서를 사용하여 연결을 종료하고 클라이언트의 요청을 암호화 해제합니다. 자세한 내용은 SSL 인증서 단원을 참조하십시오.
> + Amazon CloudWatch — 로드 밸런서를 모니터링하고 필요에 따라 조치를 취할 수 있게 해 줍니다. 자세한 내용은 Application Load Balancer의 CloudWatch 지표 단원을 참조하십시오.
> + Amazon ECS — EC2 인스턴스 클러스터에서 Docker 컨테이너를 실행, 중단 및 관리 가능합니다. 로드 밸런서를 구성하여 컨테이너에 트래픽을 라우팅할 수 있습니다. 자세한 내용은 Amazon Elastic Container Service Developer Guide에서 서비스 로드 밸런싱을 참조하십시오.
> + AWS Global Accelerator — 애플리케이션의 가용성과 성능을 향상시킵니다. 액셀러레이터를 사용하여 하나 이상의 AWS 리전에 있는 여러 로드 밸런서에 트래픽을 분산합니다. 자세한 내용은 AWS Global Accelerator 개발자 안내서 단원을 참조하십시오.
> + Route 53 — 도메인 이름(예: www.example.com)을 컴퓨터를 사용하여 서로 연결해주는 숫자로 된 IP 주소(예: 192.0.2.1)로 변환하여 방문자를 안정적이며 비용 효율적으로 웹 사이트로 라우팅하도록 합니다. AWS는 로드 밸런서와 같은 사용자의 AWS 리소스에 URL을 배정합니다. 그러나 기억하기 쉬운 URL이 필요한 경우도 있습니다. 예를 들어 도메인 이름을 로드 밸런서로 매핑할 수 있습니다.
> + AWS WAF — Application Load Balancer와 함께 AWS WAF를 사용하여 웹 ACL(웹 액세스 제어 목록)의 규칙에 따라 요청을 허용하거나 차단할 수 있습니다. 자세한 내용은 Application Load Balancer 및 AWS WAF 단원을 참조하십시오.


Amazon API Gateway
---
규모에 관계없이 자체 REST 및 WebSocket API를 생성하고 배포가능
>
>
> API Gateway는 다음을 지원하는 AWS 서비스입니다.
> + 백엔드 HTTP 엔드포인트, AWS Lambda 함수 또는 기타 AWS 서비스를 노출하기 위한 RESTful 애플리케이션 프로그래밍 인터페이스(API)의 생성, 배포, 관리.
> + AWS Lambda 함수 또는 기타 AWS 서비스를 노출하기 위한 WebSocket의 생성, 배포 및 관리.
> + 프런트 엔드 HTTP 및 WebSocket 엔드포인트를 통해 노출된 API 메서드 호출.
>
> API Gateway는 다음과 같은 RESTful API를 생성합니다.
> + HTTP 기반.
> + 상태 비저장 클라이언트-서버 통신을 활성화합니다.
> + 표준 HTTP 메서드(예: GET, POST, PUT, PATCH, DELETE)를 구현합니다.
>


NAT Gateway
---
[Document](https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/vpc-nat-gateway.html)

> + NAT 디바이스를 사용하면 프라이빗 서브넷의 인스턴스를 인터넷(예: 소프트웨어 업데이트용) 또는 기타 AWS 서비스에 연결하는 한편, 인터넷에서 해당 인스턴스와의 연결을 시작하지 못하게 할 수 있습니다.
> + NAT 디바이스는 프라이빗 서브넷의 인스턴스에서 인터넷 또는 기타 AWS 서비스로 트래픽을 전달한 다음 인스턴스에 응답을 다시 보냅니다. 트래픽이 인터넷으로 이동하면 소스 IPv4 주소가 NAT 디바이스의 주소로 대체되고, 이와 마찬가지로 응답 트래픽이 해당 인스턴스로 이동하면 NAT 디바이스에서 주소를 해당 인스턴스의 프라이빗 IPv4 주소로 다시 변환합니다.


AWS Global Accelerator
----
> AWS 글로벌 네트워크를 통해 구성한 상태, 클라이언트 위치 및 정책을 기반으로 트래픽을 최적의 지역 엔드포인트로 라우팅합니다. 이 서비스는 상태 또는 구성의 변화에 즉시 반응하여 클라이언트의 인터넷 트래픽이 항상 건강한 엔드포인트로 전달되도록 합니다.
