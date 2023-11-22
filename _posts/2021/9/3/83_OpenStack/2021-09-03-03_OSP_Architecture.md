---
layout: post
title: "[OpenStack] OSP Architecture"
description: " "
date: 2021-09-03
tags: [개발]
comments: true
share: true
---

## # Provisioning Flow

![](https://github.com/dh77hd/Note/blob/master/83_OpenStack/image/03_provisioning.PNG?raw=true)

1. Horizon 을 통해 오픈스택 접근
2. Horizon 에서는 keystone으로 인증 요청을 위해 REST call
3. 컴포넌트 간 요청에 사용되는 인증 토큰을 생성하고 사용자에게 전송
4. 대시보드 또는 CLI에서 새 인스턴스 요청 시 , 'launch instance' 또는 'nova-boot' 양식으로 작성됨. 해당 양식을  REST API로 변환하여 nova-api로 전송
5. 작업을 수행하기 전, 항상 keystone 인증이 필요하므로 인증 작업을 실시
6. 인증 요청에 성공하면 인증 토큰을 받는다.
7.  nova-api는 nova DB와 통신
8. 새 인스턴스를 위한 초기 DB 엔트리 생성
9. nova-api는 rpc.call 요청을 nova-scheduler에 전송
10. nova-scheduler는 queue에서 해당 요청을 가져옴
11. nova-secheduler가 nova-DB와 통신하면서, 필터링과 가중치를 통해 적절한 호스트(컴퓨트노드)를 찾음
12. 필터링과 가중치 적용 후, 선정된 호스트 ID를 가진 인스턴스 엔트리를 재전송
13. nova-scheduler는 선정된 호스트의 nova-compute로 인스턴스 실행을 위한 rpc.cast 전송
14. nova-compute는 queue에서 해당 요청을 가져옴
15. nova-compute는 인스턴스 정보(image, flavor 등)를 얻기 위해 nova-conductor로 rpc.call 요청 전송
16. nova-conductor는 queue에서 해당 요청을 가져옴
17. 인스턴스 정보를 찾기 위해 nova-DB와 통신
18. 찾은 인스턴스 정보를  queue에 전송하고 nova-compute는 해당 인스턴스 정보를 가져옴
19. 인스턴스 정보를 바탕으로 인스턴스 생성을 위한 작업을 시작. Image ID로 해당 Image URI 요청
20. nova-compute는 이미지 메타데이터 받음
21. IP address, subnet 등 네트워크 정보를 받기 위해 neutron-server로 API call
22. 네트워크 정보를 받음
23. 디스크 할당을 위해 cinder-api로 API call
24. 블록 스토리지 정보를 받음
25. 인스턴스 생성을 위한 정보를 바탕으로 하이퍼바이저(libvirt)에 인스턴스 생성 요청
26. 인스턴스 생성