## Insert Image Into Library

- 이미지를 라이브러리에 추가하고 코드에서 사용할 수 있도록 함

- - 프리로드 섹션에서 사용

> ```Javascript
> game.load.image(library_key,path_to_image);
> ```

 

## Add Image to the Stage

- 스프라이트를 스테이지에 추가

> ```Javascript
> this.char1=game.add.sprite(x,y,library_key);
> ```

 

## Preload Sprite Sheet

- 스프라이트 시트를 라이브러리에 미리로드함

> ```Javascript
> game.load.spritesheet('ref_name', 'pathto.png', sprite_width, sprite_height, number_of_cells);
> ```

 

## Set Sprite Top Position

- 스프라이트 맨 위의 거리를 설정함

> ```Javascript
> this.char1.y=top_postion;
> ```

#  

## Set the Left Position of a Sprite

- 스프라이트의 왼쪽 위치를 설정합니다.

> ```Javascript
> 
> ```

 

## Set the registration point for a sprite

- 스프라이트의 포인트를 설정.

- - 예를 들어 앵커를 0,0으로 설정하면 스프라이트의 왼쪽 위 모서리에 지정이 적용됨. 앵커를 0.5,0.5로 설정하면 스프라이트 중간에 위치가 작용됨.

> ```Javascript
> this.char1.x=left_position;
> ```

#  

## Add an animation to a sprite

- 스프라이트의 애니메이션을 정의

> ```Javascript
> mysprite.animations.add('walk', frame_array, frames_sec,loopBoolean);
> ```

#  

## Play an animation

- .animation.add에 의해 정의된 스프라이트에서 애니메이션을 재생함.

> ```Javascript
> mysprite.animations.play('animation name');
> ```

#  

## Add a mask to a sprite

- 그래픽을 부분적으로 가릴 마스크를 추가함

> ```Javascript
> // A mask is a Graphics object
> mask = game.add.graphics(0, 0);
> // Shapes drawn to the Graphics object must be filled.
> mask.beginFill(fill_color);
> // Here we'll draw a circle
> mask.drawCircle(left, top, radius);
> // And apply it to the Sprite
> sprite.mask = mask;
> ```

#  

## Set a sprite frame

- 간단한 이미지 대신 스프라이트 시트를 사용하는 스테이지에 스프라이트를 추가혀면 표시되는 프레임을 선택할 수 있음

> ```Javascript
> sprite.frame=frame_number;
> ```

#  

## Add a group

-  

> ```Javascript
> var myGroup=game.add.group();
> myGroup.add(sprite);
> ```

#  

## Add a Tilesprite

- 여러 개로 결합된 스프라이트를 추가
- 배경 스크롤에 사용됨

> ```Javascript
> this.tileSprite = game.add.tileSprite(x, y, width, height, 'key');
> ```

 

## Prototype template

- 이것을 사용하여 스프라이트에 대한 prefap/class만듦

> ```Javascript
> var Monster = function(x=0, y=0, frame=0) {
>     Phaser.Sprite.call(this, game, x, y, 'monster', frame);
>     // initialize your prefab here
> };
> Monster.prototype = Object.create(Phaser.Sprite.prototype);
> Monster.prototype.constructor = Monster;
> Monster.prototype.update = function() {
>     // write your prefab’s specific update code here
> };
> ```

 

## Create sprite in group

-  

> ```Javascript
> group.create(x, y,'key');
> ```

#  

## Loop through group

-  

> ```Javascript
> myGroup.forEach(function(item) {         
> }.bind(this));
> ```

#  

## Create multiple

-  

> ```Javascript
> myGroup.createMultiple(20, 'myKey', 0, false);
> ```



## Detect the end of a animation

- 에니메이션이 완료되면 함수를 호출

> ```Javascript
> myAnimation.onComplete.add(function, scope);
> ```

#  

## Load a sprite sheet with json

- JSON데이터로 스프라이트 시트를 로드

> ```Javascript
> game.load.atlasJSONHash('letters',"images/main/letters.png","images/main/letters.json");
> ```

