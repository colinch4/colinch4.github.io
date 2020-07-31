## 개요

- Phaser js로 게임을 개발할 때, Start 부분에서 사용되는 기본적인 코드에 대해 공부

 

## Blank State

- 필수 기능이 있는 빈 상태 템플릿

> ```Javascript
> var StateMain={      
>     preload:function()
>     {      
>     },  
>     create:function()
>     {      
>     },  
>     update:function()
>     {              
>     }      
> }
> ```



## Switch states

- 상태를 변경

- - 예를들어 게임이 종료 된 경우 game.state.start("StateGmeOver")를 호출할 수 있음

- > ```Javascript
  > game.state.start(state_name);
  > ```



## Start for Desktop

- Phser js를 시작하는데 필요한 기본 파일

> ```Javascript
> var game;
> window.onload = function()
> {
>     game=new Phaser.Game(480,640,Phaser.AUTO,"ph_game");
>     game.state.add("StateMain",StateMain);
>     game.state.start("StateMain");
> }
> ```



## Start for Desktop/Mobile

- 모바일을 지원하는 Phaser js를 시작하는데 필요한 기본 파일

> ```Javascript
> var game;
> var useLandscape=false;
> window.onload = function () {
>     var isMobile=navigator.userAgent.indexOf("Mobile");
>     if (isMobile>-1)
>     {
>         isMobile=true;
>     }
>     else
>     {
>         isMobile=false;
>     }
>     if (isMobile==false) {
>         //desktop laptop
>         if (useLandscape == true) {
>             game = new Phaser.Game(640, 480, Phaser.AUTO, "ph_game");
>         } else {
>             game = new Phaser.Game(480, 640, Phaser.AUTO, "ph_game");
>         }
>     } else {
>         //mobile device
>         game = new Phaser.Game(window.innerWidth, window.innerHeight, Phaser.AUTO, "ph_game");
>     }
>     game.state.add("StateMain",StateMain);
>     game.state.start("StateMain");
> }
> ```



## Basic HTML

- Phaser js용 html

> ```HTML
> <!DOCTYPE html>
> <html lang="">
>     <head>
>         <meta charset="UTF-8">
>         <title>Game Title Here</title>
>         <script src="js/phaser.min.js"></script>
>         <script src="js/main.js"></script>  
>     </head>
>     <body>
>     </body>
> </html>
> ```



## Full Screen Meta Tag

- 모바일용 전체 화면에 html을 삽입하는 메타 태그

> ```HTML
> <meta name="viewport" content="user-scalable=0, initial-scale=1,minimum-scale=1, maximum-scale=1, width=device-width, minimal-ui=1">
> ```



## Sample Init State

- 이 샘플을 사용하여 init 상태를 만듦
- 초기화 상태는 실행을 위한 베어 본 코드를 설정하고 로드 상태를 준비함

> ```Javascript
> var StateInit = {
> 
> 
>     preload: function () {
>         game.load.image("loadingEmpty", "images/loading/progress_none.png");
>         game.load.image("loadingFull", "images/loading/progress_all.png");
>         game.scale.forceOrientation(true, false);
>         game.scale.enterIncorrectOrientation.add(this.wrongWay, this);
>         game.scale.leaveIncorrectOrientation.add(this.rightWay, this);
>     }
>     , create: function () {
>         game.state.start("StateLoad");
>     }
>     , update: function () {
>     }
>     , rightWay: function () {
>         document.getElementById("wrong").style.display = "none";
>     }
>     , wrongWay: function () {
>         document.getElementById("wrong").style.display = "block";
>     }
> }
> ```



## Sample Load State

- 로드 상태는 게임을 시작하기 전에 모든 것을 미리로드 할 수 있게 함

> ```Javascript
> var StateLoad = {
>     preload: function () {
>         var empty = game.add.image(0, 0, "loadingEmpty");
>         var full = game.add.image(0, 0, "loadingFull");
>         empty.x = game.world.centerX;
>         empty.y = game.world.centerY;
>         empty.anchor.set(0.5, 0.5);
>         full.anchor.set(0, 0.5);
>         full.x = game.world.centerX - empty.width / 2;
>         full.y = empty.y;
>         game.load.setPreloadSprite(full);
>         //PRELOAD EVERYTHING HERE
>     },
>     create: function () {
>         game.state.start("StateTitle");
>     },
>     update: function () {
>     }
> }
> ```