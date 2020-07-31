## **개요**

본 문서는 rpm을 이용한 패키지 생성 및 관리방법을 설명하는 메뉴얼이다.

## **RPM 파일 생성**

**RPM 파일 생성과정은 다음과 같다.

1. RPM 패키지 제작 디렉토리 생성
2. 소스 추가 및 압축
3. 패키지에 대한 명세파일(spec) 생성
4. rpmbuild 수행하여 패키지 생성
5. rpm 파일 확인 

1. ### RPM 패키지 제작 디렉토리 생성RPM Build를 사용하기 위해서 다음과 같은 디렉토리 환경이 요구된다.

    rpmbuild
   ├── BUILD
   ├── BUILDROOT
   ├── RPMS
   ├── SOURCES
   ├── SPECS
   └── SRPMS

#### 디렉토리 설명

- **BUILD** : 소스 패키지를 풀어서 컴파일하는 디렉토리이다. 이 과정은 RPM프로그램이 알아서 해주기 때문에 특별하게 이 안에서 해 줄 일은 없다.
- **RPMS** : 최종적으로 만들어지는 RPM 파일이 존재하는 디렉토리이다. 성공적으로 패키징이 끝나면 이 디렉토리 밑에 RPM파일이 생긴다
- **SOURCES** : RPM을 만드는데 사용되는 소스가 있는 디렉토리이다 패키징을 하는 사람은 이 디렉토리에 소스파일을 복사해두어야 한다. 소스파일은 mkefile을 포함해서 tar.gz로 압축한 파일 하나만 두면 된다
- **SPECS** : RPM을 만드는 명세 파일이 들어있는 디렉토리이다. sepc 명세 파일은 패키징을 하는 사람이 직접 만들어주어야 한다.
- **SRPMS** : 소스 RPM이 있는 디렉토리이다

#### 2. 소스 추가 및 압축

- **SOURCE디렉토리에** 패키지에 필요한 소스를 tar.gz로 압축하여 복사한다. (tar -czvf 사용)

#### 3. 패키지에 대한 명세파일(spec) 생성

- **SPECS디렉토리에** 명세파일(.spec)을 생성한다spec파일은 rpm을 만드는 내용이 들어있다vim에디터로 .spec파일을 생성할 시 자동으로 기본 템플릿을 채워준다

sepc파일 기본 템플릿

```spec
Name:
Version:
Release:    1%{?dist}
Summary:
Group:
License:
URL:
Source0:
BuildRoot:   %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:
Requires:
%description
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%cleanrm -rf $RPM_BUILD_ROOT
%files
%defattr(-,root,root,-)
%doc
%changelog**Name****
**RPM 패키지의 이름을 설정한다.
```

**Version****
**생성되는 패키지의 버전 정보를 설정한다. 여기에 설정된 버전 정보는 패키지 레이블 및 패키지 filename 에 설정되게 된다. (version 0 인 경우 초기설치, version 1인 경우 patch)

**Release****
**Release 번호는 이 패키지가 현재 버전에서 몇번째 릴리즈 되었는지를 나타낸다. 패키지 레이블은 버전 정보와 릴리즈 번호가 합쳐져서 나타난 정보이다.

**Summary****
**패키지의 간단한 설명 정보이다.

**Group****
**Group 은 해당 패키지가 어떤 종류의 소프트웨어 인지를 나타낸다.

**License****
**라이센스 정보를 나타낸다. Copyright 와 비슷하다.

**URL****
**해당 소프트웨어의 더욱 자세한 정보를 알수 있는 URL 정보를 입력한다.

**Source****
**RPM을 만들기 위해 사용할 압축파일(*.tar.gz)를 지정한다. Source 뒤에 숫자를 붙여 여러 소스파일을 지정해 줄 수 있다. 숫자는 '0'부터 시작해야 한다.

**BuildRoot****
**RPM 파일 빌드에 사용할 루트 디렉토리를 지정한다. RPM 패키지를 빌드할 때 소스를 컴파일하고 컴파일한 프로그램을 BuildRoot 필드가 지정하는 디렉토리를 루트 디렉토리(/)로 간주하여 설치한다. 이렇게 설치된 디렉토리 구조를 묶어서 CONTENTS.cpio 파일을 만들어 RPM 파일을 만들게 된다.

**BuildRequires****
**때로는 RPM을 Build 하기 위해서도 필요한 패키지가 있을 수 있다. RPM을 Build 하기 위해 필요한 RPM 패키지를 지정한다.

**Requires****
**생성되는 RPM 의 설치 의존성을 설정한다. 기본적으로는 이름만 써도 되지만, 버전을 체크하도록 할 수 있다. 비교 연산자로는 (>, <, =, >=, <=)를 지원한다.

**%description****
**패키지에 대한 상세 설명을 설정한다.


**%prep****
**Source0에서 지정한 파일을 빌드를 하기 위해 필요한 일들을 지정해 줍니다. 압축을 푸는 작업이 주된 작업이 된다.

**%build****
**'%prep' 다음에 수행되며, 압축을 푼 소스를 가지고 빌드를 수행한다.
주로 './configure'를 실행하여 'Makefile'을 생성하고, 'make'를 수행하여 빌드를 수행한다.

**%install****
**'%build' 다음에 수행되며, 빌드 수행결과 생성된 파일들을 설치 폴더로 복사하는 역할을 수행한다.주로, 'make install'을 수행해서 실행 파일들을 '~/rpmbuild/BUILDROOT' 폴더 아래로 넣는 작업을 수행한다.
일반적으로 빌드를 통해 생성된 실행 파일을 특정 경로에 넣어주는 작업을 설정해주게 한다.

**%clean****
**빌드 마지막에 수행한다. 빌드 과정에서 생긴 파일들을 지우도록 설정 할 수 있으며, 주로 설치 폴더를 삭제하도록 설정해준다. (spec파일 기본 탬플릿에 있는 내용을 그대로 사용하시면 된다)

**%files****
**rpm 파일에 묶여야(패키징) 하는 파일의 이름을 지정해주게 된다. 물론, 폴더 이름을 지정 해주는 것도 가능한데, 하위 폴더를 포함 한 모든 파일을 모두 묶는 의미로 사용된다. 여기서 지정한 파일만 rpm 파일에 묶이게 된다고 생각하면 된다.

**%attr****
**설치된 rpm 권한과 소유권을 지정해 줄 수 있다.
%attr (<mode>, <user>, <group>) filename 

**%defattr****
**기본 권한 값을 설정 해 줄 수 있다.
**%doc****
**소스 패키지 내의 문서 파일을 지정하는데 사용된다.

**%config****
**기존에 설치 된 파일이 수정되었다면 기존 파일을 '.rpmsave' 확장자를 붙여서 백업해놓고 새로운 파일을 설치한다. 설치 이후에 파일이 수정되었다면 변경된 설정 값을 지우지 않고 백업해 준다는 의미

**%config(noreplace)**기존에 설치 된 파일이 수정되었다면 기존 파일을 유지하고, 새로 설치될 파일을'.rpmsave' 확장자를 붙여서 설치합니다. 설치 이후에 파일이 수정되었다면 수정된 설정 값을 유지 시키기 위해 사용합니다.
 **옵션 이름****RPM에 포함된 파일 수정 여부****설치된 파일 편집 안됨** **설치된 파일 편집 됨** [기본]No RPM으로 부터 설치 RPM으로 부터 설치 YesRPM으로 부터 설치 RPM으로 부터 설치 %config No RPM으로 부터 설치 기존 파일 유지 Yes RPM으로 부터 설치 RPM으로 부터 설치 기존 파일은 .rpmsave로 이름수정 %config(noreplace) No RPM으로 부터 설치 기존 파일 유지 Yes RPM으로 부터 설치 기존 파일 유지. RPM에서 받아온 파일은 .rpmnew로 저장. 

**%dir****
**패키지에 포함시킬 폴더를 지정해줘서 생성하도록 한다. 주로 특정 위치에 빈 폴더를 생성 시키기 위해 사용한다. 

**%post****
**RPM 설치 이후에 뭔가 추가 작업을 해줘야 할 때 사용한다. 예를 들면 설정 파일에서 값을 변경하거나, chkconfig 와 같은 작업 지정이 가능하다.



**spec파일 예시**

```spec
Name:    core_acs_media_engine
Version:    ACS_C_R0.9.0rc1_0
Release:    0
Summary:    core_acs_media_engine-ACS_C_R0.9.0rc1_0

Group:        AMF    
License:    GPL
URL:        www.uangel.com
Source0:    %{name}-%{version}.tar.gz    
BuildRoot: 	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:    /bin/rm, /bin/mkdir, /bin/cp, /bin/ln, /bin/chown, /bin/chmod
Requires:    /bin/bash

%description
A core acs media engine package

%prep
%setup -q

%build
\#configure
\#make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/home/amf/amf/cache
mkdir -p $RPM_BUILD_ROOT/home/amf/amf/alarm

cp -f bin/mdaegn $RPM_BUILD_ROOT/home/amf/amf/bin/
cp -f bin/logleveler $RPM_BUILD_ROOT/home/amf/amf/bin/

 
%post
ln -s $RPM_BUILD_ROOT/home/amf/amf/bin/mdaegn $RPM_BUILD_ROOT/home/amf/amf/bin/mdaegn_0
chown -R amf:acs $RPM_BUILD_ROOT/home/amf/amf/bin/mdaegn_0

 
%files
%defattr(755,amf,acs,755)%config(noreplace)/home/amf/amf/cache%config(noreplace)/home/amf/amf/alarm%config(noreplace)/home/amf/amf/stat%config(noreplace)/home/amf/amf/logs%config(noreplace)/home/amf/amf/config%config(noreplace)/home/amf/amf/prompts%config(noreplace)/home/amf/amf/bin/*
%doc
%attr(755,amf,acs)/home/amf/amf
%attr(755,amf,acs)/home/amf/amf/bin
%attr(755,amf,acs)/home/amf/amf/stat/
 
%changelog**
```



#### 4. **rpmbuild 수행하여 패키지 생성

명세파일(.spec)을 이용하여 실제 RPM파일을 생성한다

- rpmbuild -ba <spec파일>

#### 5. rpm 파일 확인

RPMS**디렉토리에 rpm파일이 정상적으로 생성되었는지 확인한다.





## **메이븐 플러그인을 사용한 RPM 생성**

메이븐 플러그인을 사용해 손쉽게 RPM 생성 및 관리가 가능하다
- (rpm-maven-plugin은 rpmbuild를 사용하므로 rpmbuild를 먼저 설치해야 rpm-maven-plugin이 올바르게 동작한다)
- pom.xml작성법
(rpm package는 여러가지 기능을 수행할 수 있지만 여기선 기본적인 file copy내용을 다룬다.)

```xml
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>rpm-maven-plugin</artifactId>
  <version>2.0.1</version>
  <configuration>
    <copyright>[저작권자]</copyright>
    <group>[그룹명]</group>
    <release>[릴리즈 버전]</release>
    <defaultDirmode>[기본 경로 권한 ex)755]</defaultDirmode>
    <defaultFilemode>[기본 파일 권한 ex)644]</defaultFilemode>
    <defaultUsername>[계정 명]</defaultUsername>
    <defaultGroupname>[그룹 명]</defaultGroupname>
    <mappings>
      <mapping>
        <configuration>[true/false/noreplace]</configuration>
        <directory>[파일 복사 위치]</directory>
        <sources>
          <source>
            <location>[복사할 대상]</location>
          </source>
        </sources>
      </mapping>
    </mappings>
  </configuration>
</plugin>
```

 **<mapping> 요소**

- <configuration> : .spec파일의 <%config>에 해당하는 요소. “noreplace”인 경우 파일을 덮어씌우지 않는다.
- <directory> : 파일 복사 위치. RPM 설치 과정에서 생성한다.
- <filemode> : 파일의 권한 모드
- <sources> : 해당 복사 위치에 넣을 대상



**요소 문서 링크**

- https://www.mojohaus.org/rpm-maven-plugin/params.html



**pom.xml 예시**

```xml
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>rpm-maven-plugin</artifactId>
  <version>2.0.1</version>
  <configuration>
    <copyright>2020, Uangel</copyright>
    <group>Service Dev</group>
    <release>${rpm.release.version}</release>
    <defaultDirmode>755</defaultDirmode>
    <defaultFilemode>644</defaultFilemode>
    <defaultUsername>amf</defaultUsername>
    <defaultGroupname>acs</defaultGroupname>
    <mappings>
      <mapping>
        <directory>/home/amf/amf/lib/</directory>
        <sources><source>
          <Location>${project.basedir}/target/core-acs_amf-jar-with-dependencies.jar</location>
          </source></sources>
      </mapping>
      <mapping>
        <directory>/home/amf/amf/bin/</directory>
        <filemode>755</filemode>
        <sources>
          <source>
            <location>${project.basedir}/src/main/resources/bin/amf.sh</location>
          </source>
          <source>
            <location>${project.basedir}/src/main/resources/bin/scp.sh</location>
          </source>
        </sources>
      </mapping>
      <mapping>
        <configuration>noreplace</configuration>
        <directory>/home/amf/amf/config/</directory>
        <sources>
          <source>
            <location>${project.basedir}/src/main/resources/config/c-acs_amf_user.config</location>
          </source>
        </sources>
      </mapping>
    </mappings>
  </configuration>
</plugin>
```



### **RPM 설치/조회/삭제

- **설치 및 업데이트**
  - `$ rpm -Uvh <rpm 파일명>`
- **조회**
  - `$ rpm - qa | grep <패키지명>`
- **삭제**
  - rpm -ev <패키지명>