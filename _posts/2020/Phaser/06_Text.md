## Add Text

- 스테이지에 텍스트 입력란 추가

> ```Javascript
> var myText=game.add.text(x,y,text);
> ```

 

## Center text

- x 앵커를 너비의 50%로 설정하여 텍스트 위치를 가운데로 맞춤

> ```Javascript
> myText.anchor.x = Math.round(myText.width * 0.5) / myText.width;
> ```

 

## Text font

- 텍스트의 폰트명 설정

> ```Javascript
> myText.font="font_name";
> ```

 

## Set Text color

- 텍스트 필드 색상을 설정

> ```Javascript
> myText.fill="#textColor";
> ```

 

## Font size

- 텍스트 필드의 글꼴 크기를 설정

> ```Javascript
> myText.fontSize=64;
> ```

 

## Fancy Fonts

- 텍스트 추가 기능의 네 번째 배개 변수를 사용하여 고급 글꼴 속성을 설정

> ```Javascript
> this.titleText=game.add.text(x,y,text,{ font: "size fontName", fill: "color", stroke: "color", strokeThickness: number, align:string });
> ```