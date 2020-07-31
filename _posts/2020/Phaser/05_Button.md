## Add a button

- 버튼 추가

> ```Javascript
> game.add.button(x,y,imageKey,clickFunction,this,over_frame,normal_frame,down_frame)
> ```

 

## Sprite click

-  

> ```Javascript
> this.char1.events.onInputUp.add(this.clickHandler,scope);
> ```

#  

## Enable a sprite for input

- 스프라이트에서 클릭 이벤트를 사용할 수 있으려면 먼저 입력에 사용하도록 설정해야 함.

> ```Javascript
> this.spriteName.inputEnabled=true;
> ```

 

## Canvas click

- 전체 게임에 리스너 추가

> ```Javascript
> game.input.onUp.add(functionName, this);
> ```