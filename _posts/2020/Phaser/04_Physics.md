## Start the physics engine

- Arcade     Physics 엔진 시작

> ```Javascript
> game.physics.startSystem(Phaser.ARCADE);
> ```

 

## Enable an object for physics

- Phaswer에게 선택된 객체에 물리엔진을 사용하도록 알려줌

> ```Javascript
> game.physics.enable(sprite, Phaser.Physics.ARCADE);
> ```

 

## Set velocity

- 개체의 속도를 설정

> ```Javascript
> this.char.body.velocity.setTo(200,200);
> ```

 

## Set bounce

- 개체가 충돌할 때 바운스를 설정

> ```Javascript
> this.body.bounce.set(1,1);
> ```

- 1은 100%바운스/ .5는 50%

 

## Set Global Gravity

- 모든 개체의 기본 중력 설정

> ```Javascript
> game.physics.arcade.gravity.y = 100;
> ```

 

## Set object gravity

- 개별 스프라이트의 중력 설정

> ```Javascript
> this.char.body.gravity.y = 50;
> ```

 

## Set group physics

- 그룹에 물리엔진을 설정

> ```Javascript
> myGroup.enableBody = true;
> myGroup.physicsBodyType = Phaser.Physics.ARCADE;
> ```