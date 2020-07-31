## KVM이란

- Kernel Virtual Machine
- Linux를 하이퍼바이저로 전환하여 호스트 머신이 게스트 또는 가상 머신을 하나 이상 실행할 수 있게 해줌
  - 호스트머신 : H/W에 기본적으로 설치된 OS가 동작하는 머신
  - 게스트머신/가상머신 : 호스트 머신의 운영체제 위에서 종작하는 머신. 다른 호스트 OS와 다른 OS로도 게스트 머신 설치 가능



## 설치

1. KVM관련 패키지 설치

> ```shell
> $ yum install qemu-kvm libvirt virt-install bridge-utils virt-manager
> ```

1. KVM모듈 확인

> ```shell
> $ lsmod | grep kvm
> ```

1. libvirtd 실행 및 확인

> ```shell
> $ systemctl start libvirtd
> $ systemctl enable libvirtd
> $ systemctl list-unit-files | grep libvirtd
> ```

1. 브릿지 네트워크 설정

   1.  Virbr0 제거
      1. 
   2. eth0dml dhcp를 지우고 brr0로 Bridged한다

   > 수정
   >
   > ```shell
   > BRIDGE=br0 
   > NM_CONTROLLED=no 
   > ```

   3. br0를 만든다

   > 다음과 같이 생성
   >
   > ```shell
   > DEVICE=br0 
   > TYPE=Bridge 
   > BOOTPROTO=dhcp 
   > ONBOOT=yes 
   > DELAY=0 
   > NM_CONTROLLED=no 
   > ```

   4. 네트워크 재시작

   > ```shell
   > $ chkconfig NetworkManager off 
   > $ chkconfig network on 
   > $ service NetworkManager stop 
   > $ service network restart
   > ```

5. 가상 머신 설치

> ```shell
> $ virt-install \
> --name centos67 \
> --ram 1024 \
> --disk path=/VM/centos67.img,size=10 \
> --vcpus 1 \
> --os-type linux \
> --network bridge=br0 \
> --graphics none \
> --console pty,target_type=serial \
> --location /var/kvmimg/CentOS-7-x86_64-DVD-2003.iso \
> --extra-args 'console=ttyS0,115200n8 serial'
> ```

| 옵션            | 설명                                                         |
| --------------- | ------------------------------------------------------------ |
| --name          | VM Name                                                      |
| --ram           | Memory size Mbyte단위                                        |
| --disk          | VM이 생성되는 이미지 파일 위치 및 사이즈 (여기서 사이즈는 VM의 Disk 사이즈임) |
| --vcpus         | VM이 사용할 cpu(core) 갯수                                   |
| --os-type       | OS  타입  window, linux                                      |
| --os-variant    | 게스트를 설치 중인 OS 변수, OS 종류 centos7.0 , rhel7 등 (정보 확인은  "osinfo-query os" 통해 확인) |
| --network       | Bridge interface 또는 Vm 사용할 인터페이스 나 네트워크 정보 "virt-install --network help" 로 자세한 정보 확인 가능 |
| --graphics      | GUI 옵션으로 CLI작업시에는 보통 none으로 설정                |
| --console       | 호스트 머신과 게스트 머신 사이의 console  연결 설정          |
| --extra-args    | --location에서 부팅된 설치 커널에 전달할 추가 인수           |
| --location      | 설치할 O, 즉 소스 이미지 위치와 이름                         |
| --noautoconsole | 게스트 콘솔에 자동으로 연결하지 마십시오.                    |
| --noreboot      | 설치를 완료한 후 게스트를 부팅하지 마십시오.                 |

6. 시작 및 기타 명령어

- console 접속 및 빠져나오기

  - ```shell
    $ virsh console [가상머신 이름]
    ```

- 생성된 VM리스트 확인

    - ```shell
      $ virsh list
      ```

- 가상 머신 시작

    - ```shell
      $ virsh start [가상머신 이름]
      ```

- 가상 머신 종료

    - ```shell
      $ virsh shutdown [가상머신 이름]
      ```

- 가상 머신 재부팅

    - ```shell
      $ virsh reboot [가상머신 이름]
      ```

- 가상 머신 강제 종료

    - ```shell
      $ virsh destroy [가상머신 이름]
      ```

- 가상 머신 삭제 - 가상 머신 종료 후 사용 / 확인과정 없이 바로 삭제됨 / 가상 머신 이미지는 직접 삭제해야함

    - ```shell
      $ virsh undefine [가상머신 이름]
      $ rm [가상머신 이미지 경로]
      ```