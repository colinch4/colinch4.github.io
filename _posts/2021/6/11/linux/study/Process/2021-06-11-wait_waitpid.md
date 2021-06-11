---
layout: post
title: "[linux] wait() , waitpid() 함수"
description: " "
date: 2021-06-11
tags: [linux]
comments: true
share: true
---

# wait() , waitpid() 함수

## ⇒ 종료된 자식 프로세스의 리턴값 요청 함수

- 좀비 프로세스(zombie process)

: 프로세스 종료 후 메모리 상에서 사라지지 않는 프로세스 

- 좀비 프로세스 생성 이유

: 자식 프로세스가 종료하면서 SIGCHLD 시그널을 커널을 통해 부모 프로세스에 전달한 후, 부모가  wait()이나 waitpid()로 자식의 리턴값(성공적으로 종료하면 값은 0)을 받아야 자식 프로세스를 소멸시킬 수 있다. 

: 하지만 반환값을 부모 프로세스에 전달하지 못한 경우 **자식 프로세스는 좀비로 존재하고 소멸되지 않는다.**(좀비프로세스로 있다가 부모 프로세스가 종료 후에야 소멸된다.)

: 부모 프로세스가 커널에게 종료된 자식 프로세스의 리턴값을 **전달 요청**을 해야만 커널은 자식의 리턴값을 부모에게 전달 가능함.(wait(), waitpid()을 통해 전달요청 가능)

**좀비 프로세스가 생기는 경우**
```
      # include <stdio.h>
      # include <stdlib.h>
      # include <unistd.h>
      
      int main(){
      
        pid_t fork_ret;
      
        fork_ret = fork();
      
        if(fork_ret >0){
          printf("Parent_my pid: %d Child_pid: %d \n", getpid(), fork_ret);
          sleep(60);
          exit(0);
        }else if(fork_ret == 0){
          printf("Chile_my pid: %d Parent_pid: %d \n", getpid(), getppid());
          exit(0);
        }else{
          perror("fork fail!");
          exit(1);
        }
      
        return 0;
      }
    //실행내용:
    //Parent_my pid: 18195 Child_pid: 18196 
    //Chile_my pid: 18196 Parent_pid: 18195
    //=> 에서 부모 프로세스(sleep(60))을 계속 기다린다. 
    
    //확인해보면 좀비 프로세스가 생겼음을 알 수 있다. 
    //kimdo    17813  0.0  0.0      0     0 pts/1    Z+   16:48   0:00 [zombie] <defunct>
```
- 위의 코드의 경우 , 부모 프로세스가 **자식 프로세스의 반환값을 전달요청하지 않았으므로** 자식의 반환값을 못받아 자식프로세스가 수행을 다했음에도 소멸하지 못하고 좀비 프로세스가 되어버린 경우이다.
- 좀비 프로세스는 메모리를 차지하지 않고 디스크 용량, IO, CPU 시간 또한 전혀 차지 하지 않으므로 별 문제가 되어 보이지 않지만 **이들은 프로세스 테이블의 용량을 차지한다.** 자식 프로세스를 많이 만들어내고 이 프로세스들이 모두 좀비 프로세스가 되는 경우라면 프로세스 테이블의 용량이 꽉차 이후 프로세스 테이블을 사용할 수없기 때문에 좀비 프로세스는 만들지 않는 것이 좋다.
- 좀비 프로세스의 해결책으로 wait(), waitpid() 가 있다.

 

# ⇒ 좀비 프로세스가 생기지 않으려면 wait()이나 waitpid()를 통해 부모 프로세스가 자식의 리턴값을 받아야 한다.

# 1. wait()
```
    # include <sys/types.h>
    # include <sys/wait.h>
    
    pid_t wait(int *status);
```
⇒ 성공시 종료된 자식 프로세스 ID, 실패시 -1 반환. 

- status: 포인터 status가 가리키는 변수에 자식 프로세스 종료시 리턴하거나 exit 함수 호출시 전달한 인자값이 저장됨(자식은 커널을 통해 SIGCHLD 시그널을 부모 프로세스에게 보낸다.)
- 매크로 함수 WEXITSTATUS(status)로 종료시 리턴값이나 exit()인자로 넘겨진 값 확인
- 호출 시점에 종료된 자식 프로세스가 없으면 blocking 상태에 빠진다. ⇒  **부모 프로세스가 wait()으로 인해 자식 프로세스가 종료될때까지 기다린다.**
```
      # include <unistd.h>
      # include <sys/wait.h>
      # include <stdlib.h>
      # include <stdio.h>
      
      int main(){
      
        pid_t fork_ret;
        fork_ret = fork();
      
        if(fork_ret >0){//부모 프로세스
          int status;
          wait(&status);
      
          printf("status: %d \n", status);
      
          printf("parent process...\n");
          exit(0);
      
          exit(0);
        }else if(fork_ret ==0){ //자식 프로세스
          printf("child process...\n");
          sleep(5);
      
        }else{ //포크 실패 
          perror("fork error");
          exit(1);
      
        }
      
        return 0;
      }
``` 

- wait() 을 통해 부모 프로세스는 자식의 리턴값을 받게된다. 따라서 자식 프로세스는 리턴값을 부모에게 주었으므로 **좀비 프로세스가 되지않고 소멸될 수 있다.**
- wait을 통해 자식의 리턴값의 위의 코드는 status로 받는데, 자식 프로세스가 정상 종료하면 status는 리턴값을 0을 받게 되고 비정상 종료하면 리턴값이 0이 아닌 값을 받는다.(예를 들어, exit(0)이 아닐 때)
- 하지만, wait()은 부모 프로세스를 **자식 프로세스가 종료될때까지 대기하게 하므로 부모와 자식이 병행 수행할 수 없는 단점을 가지고 있다.**

## wait()의 해결책
```
       #include <unistd.h>
       #include <sys/wait.h>
       #include <stdio.h>
       #include <stdlib.h>
       
       // 자식 프로세스는 자신이 종료될 때, 부모 프로세스에게 SIGCHLD 시그널을 전달
        한다.
       void foo(int signum) {
         printf("자식 죽음...\n");
         int status;
        wait(&status);
        printf("status: %d\n", status);
       }
      
       int main() {
        signal(SIGCHLD, foo);
        int i;
        pid_t pid;
      
        pid = fork();
        if (pid > 0) {  // 부모 프로세스
          // int status;
          // wait(&status);
         // printf("status: %d\n", status);
      
          for (i = 0; i < 30; ++i) {
            printf("parent process..\n");
            sleep(1);
          }
          exit(0);
      
        } else if (pid == 0) { // 자식 프로세스
          for (i = 0; i < 3; ++i) {
            printf("child process..\n");
            sleep(1);
          }
          exit(0);
      
        } else {
          perror("fork");
          exit(1);
        }
        // fork()가 반환될 때, 자식 프로세스도 fork() 함수를 반환한다.
        printf("hello, world...\n");
      
       }
```
- 자식 프로세스가 종료가 되면 커널을 통해 SIGCHLD 시그널(17)을 보내게되는데 이를 이용해 시그널 핸들러를 만들어 wait()이 있음에도 부모와 자식이 병행수행하게 할 수 있다.
- 헤더함수 \<signal.h>를 이용해 signal()함수를 이용하고 또 그안에 매개변수로 foo함수를 이용해 SIGCHLD 값을 받는다.(int signum으로 받는데 SIGCHLD 의 값은 17이다.)  이후 foo함수에 wait()함수를 작성하여 자식 프로세스의 리턴값을 받는다.
- 이 방법은 부모 프로세스가 자식과 상관없이 코드를 수행하다 자식이 종료하면 그때 signal()가 동작해 자식 프로세스의 리턴값을 받게 한다. **따라서 부모와 자식이 병행 수행하다 자식프로세스가 좀비 프로세스로 되는 것 없이 소멸시킬 수 있다는 것이다.**

## 그러나 또 문제점
```
     #include <unistd.h>
     #include <sys/wait.h>
     #include <stdio.h>
     #include <stdlib.h>
       
     // 시그널의 한계
     //  => 시그널이 동시에 발생하면, 하나만 처리된다.
     //  => 시그널 핸들러 안에서는 절대 블록되는 함수를 호출하면 안된다.
     //   : 시그널 핸들러안에서 블록되면, 시그널 핸들러를 호출한 프로세스가 대기하게 된다.
     
     void foo(int signum) {
        int status;
        wait(&status);
        printf("status: %d\n", status);
     }
      
      
     int main() {
       signal(SIGCHLD, foo);
       int i;
       pid_t pid;
      
       for (int j = 0 ; j < 30; ++j) {
         pid = fork();
         if (pid == 0) {
            for (i = 0; i < 3; ++i) {
              printf("child process..\n");
              if (j > 5) {
                sleep(1);
              }
            }
            exit(0);
       }
      
       for (i = 0; i < 30; ++i) {
          printf("parent process..%d\n", i);
          sleep(1);
        }
        exit(0);
      
      }
```  

- **하지만 시그널 핸들러도 자식 프로세스가 여러개인 경우 문제가 생긴다.** SIGCHLD 시그널은 한 순간 한번만 사용될 수 있으므로, 만약 하나의 자식 프로세스가 종료되고 SIGCHLD 시그널을 사용중이라면 다른 자식 프로세스가 SIGCHLD 시그널를 사용할 수 없으므로 리턴값을 못보내 좀비프로세스가 되어버리는 문제점이 생겨버린다.
- 위의 경우는 fork()가 10번 호출되지만, status는 10번 아래로 출력이 되므로(=자식의 리턴값 받는 횟수가 10이 안된다.)  좀비 프로세스가 발생한다. 좀비 프로세스가 생기지 않는 해결책을 찾아야 한다.

## 해결책

```    
     void foo(int signum) {
        int status;
        while (wait(&status) > 0) {
          printf("status: %d\n", status);
        }
     }
```
- 시그널을 한 순간 한번만 사용할 수 있더라도, foo함수에 while(wait(&status)>0)을 사용하면 모든 자식 프로세스의 리턴값을 받을 수 있다. wait()의 리턴값은 성공적으로 리턴받은 자식의 pid(>0)값을 리턴하는데 while(wait(&status)>0)구문을 통해 자식 프로세스가 동시에 리턴값을 부모에게 줘도 반복해서 받을 수 있기 때문에 모든 자식의 리턴값을 받을 수 있다.

# 또 문제점

- 하지만 wait() 자체적으로 문제가 있는데 , wait()은 **블록함수**라서 부모 프로세스는 foo()를 호출해서 wait()을 호출할 때, **자식프로세스가 값을 반환하지 않았다면 종료될때까지(즉 리턴값을 받을때까지) 계속 프로세스가 블록(대기)해야한다.** (while문이 있어서 wait()을 계속 호출하므로 연달아 자식 프로세스가 종료되는 경우 wait()이 자식의 리턴값을 받을때까지 부모는 대기해야 한다.) ⇒ 물어보기
- 따라서 처음에는 부모와 자식이 동시에 수행되다가 wait()을 호출할때는 부모가 기다려야 하므로 부모가 수행되지 않는 것이다. 이것은 부모 프로세스를 사용할때 큰 낭비이므로, **블록함수인 wait()을 사용하지 않고, 비블록함수인 waitpid()을 사용해 문제를 해결한다.**

실행결과
```
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    status: 0
    child process..
    status: 0
    status: 0
    child process..
    child process..
    child process..
    status: 0
    status: 0
    child process..
    child process..
    child process..
    child process..
    child process..
    status: 0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    status: 0
    status: 0
    status: 0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    parent process..0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    parent process..1
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    parent process..2
    child process..
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    status: 0
    /*
    위의 status의 값이 연달아 나올때 부모가 수행할 시간이 충분히 있음에도 불구하고 wait()함수로 인해 
    리턴값을 받을 때까지 블록킹 되므로 부모가 수행되지 않는다. 
    */
    parent process..3
    parent process..4
    parent process..5
    parent process..6
    parent process..7
    parent process..8
    parent process..9
    parent process..10
    ^C
```
# 2. waitpid()

```
    # include <sys/types.h>
    # include <sys/wait.h>
    
    pid_t waitpid(pid_t pd, int *status, int options);
```
⇒ 성공시 종료된 자식 프로세스 ID(경우에 따라 0), 실패시 -1 리턴 

- pid : 종료 확인을 원하는 자식 프로세스 ID, 임의의 자식 프로세스인 경우 -1 대입.
- sstatus: wait 함수의 status 와 같은 역할
- options: sys/wait.h에 정의된 'WNOHANG' 상수를 인자로 전달하게 되면 이미 종료한 자식 프로세스가 없는 경우  blocking 상태로 가지않고 바로 리턴함. 이때 waitpid 함수의 리턴값은 **0**이 된다.

```
     #include <unistd.h>
     #include <sys/wait.h>
     #include <stdio.h>
     #include <stdlib.h>
       
       
      
     void foo(int signum) {
       int status;
       while (waitpid(0, &status, WNOHANG) > 0) {
          printf("status: %d\n", status);
        }
     }
      
     int main() {
       signal(SIGCHLD, foo);
       int i;
       pid_t pid;
      
       for (int j = 0 ; j < 30; ++j) {
          pid = fork();
          if (pid == 0) { //자식 프로세스 
            for (i = 0; i < 3; ++i) {
              printf("child process..\n");
              if (j > 5) {
                sleep(1);
              }
            }
            exit(0);
       }
       // 부모 프로세스 
       for (i = 0; i < 30; ++i) {
          printf("parent process..%d\n",i);
          sleep(1);
       }
        exit(0);
      
    }
```  

- waitpid에 세번째 인자로 WNOHANG을 넣으면 , **기다리는 자식의 프로세스가 종료되지 않아 리턴값을 받을 수 없는 상황일때 wait()처럼 기다리지 않고 바로 0을 반환한다.**
- 따라서 부모는 waitpid()가 호출될때 wait()처럼 자식의 리턴값을 받을때까지 기다리지 않아도 되므로 자신의 일을 수행할 수 있게된다. 즉 병행 작업이 훨씬 원활히 이루어지게 된다.

실행내용
```
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    status: 0
    status: 0
    status: 0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    status: 0
    status: 0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    status: 0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    parent process..0
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    parent process..1
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    child process..
    parent process..2
    child process..
    child process..
    child process..
    status: 0
    status: 0
    status: 0
    status: 0
    parent process..3
    status: 0
    parent process..4
    status: 0
    parent process..5
    status: 0
    parent process..5
    status: 0
    parent process..6
    status: 0
    parent process..7
    status: 0
    status: 0
    parent process..8
    status: 0
    parent process..9
    status: 0
    status: 0
    status: 0
    parent process..10
    status: 0
    parent process..11
    status: 0
    parent process..12
    status: 0
    status: 0
    parent process..13
    status: 0
    parent process..14
    status: 0
    parent process..15
    status: 0
    status: 0
    parent process..16
    status: 0
    /*
    위의 status의 값이 연달아 나올때 부모가 수행할 시간이 충분히 있어서 waitpid()는 리턴값을 받을때까지 
    기다리지않고 바로 0을 리턴해 부모가 사이사이 수행됨을 볼 수 있다. 
    위의 wait() 실행내용과 확연히 다른 양상을 보임을 알 수 있다.  
    */
    parent process..17
    parent process..18
    parent process..19
    parent process..20
    ^C
```    
