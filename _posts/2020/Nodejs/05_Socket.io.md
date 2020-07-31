## 클라이언트

- socket.on과 socket.emit만 있으면 됨!

- 소켓 설정

  > ```Javascript
  > var socket = io.connect('서버 주소');
  > socket.on('서버에서 받을 이벤트명', function(데이터) {
  >        // 받은 데이터 처리
  >        socket.emit('서버로 보낼 이벤트명', 데이터);
  > });
  > ```

* 설정

  > ```Javascript
  > io('주소', { 설정명: '설정값' }); // 클라이언트 설정
  > SocketIo(server, { 설정명: '설정값' }); // 서버 설정
  > ```

* 순수 웹소켓만 사용할 경우

  > ```Javascript
  > io('주소', { transports: ['websocket'] });
  > ```

* socket.io와 express-session 연동 예시

  > ```Javascript
  > io.use((socket, next) => {
  >     require('express-session')(옵션)(socket.request, socket.request.res, next);
  > });
  > ```



## 서버

* 서버에서 작성하는 코드 예시

  > ```Javascript
  > io.on('connection', (socket) => {
  >     socket.on('disconnect', () => {
  >         console.log('disconnected');
  >     });
  > });
  > ```

  * io는 socket.io패키지를 import한 변수
  * socket은 커넥션이 셩공했을 때 커넥션에 대한 정보를 담고 있는 변수
  * socket변수를 사용해 서버에서 이벤트 리스너를 등록하면 됨.
    * 몇 개의 이벤트는 이미 예약되어 있는데 예시로 'disconnect이벤트는 클라이언트와의 연결이 끊어졌을 때 발생

 

## 네임스페이스

- 전체에게 메시지를 보내는 것은 사실 /네임스페이스에게 메시지를 보내는 것.

- 네임스페이스를 사용하면 필요한 사람들에게만 메시지를 보낼 수 있음.

- 네임스페이스를 바꾸려면 서버에서는 of메서드를 사용

- 서버에서 네임스페이스 사용

  > ```Javascript
  > const chat = io.of('/chat');
  > chat.on('connection', (socket) => {
  > ...
  > });
  > ```

* 클라이언트에서 네임스페이스 사용

  > ```Javsacript
  > io.connect('주소/chat', 설정);
  > ```



## 클라이언트에서 메시지를 보내는 방법

- 전체에게 메시지 보내기

  > ```Javascript
  > io.emit('이벤트명', 데이터);
  > ```

  - 또는

  > ```Javascript
  > io.sockets.emit('이벤트명', 데이터);
  > ```

* 나를 제외한 전체엑 메시지 보내기

  > ```Javascript
  > socket.broadcast.emit('이벤트명', 데이터);
  > ```

  * io를 사용하지 않고 socket에 있는 boradcast객체 사용

* 특정인에게 메시지 보내기

  > ```Javascript
  > io.to(소켓아이디).emit('이벤트명' 데이터);
  > ```

* 특정 그룹에게 밋지ㅣ 보내기

  * 그룹에 들어가기나 나가기

    > ```Javascript
    > socket.join(방의 아이디); // 그룹에 들어가기
    > socket.leave(방의 아이디); // 그룹 떠나기
    > ```

    * 방의 아이디는 단순한 문자열

  * 그룹 전체, 또는 나를 제외한 그룹 전체에게 미시지 보내기

    > ```Javascript
    > io.to(방의 아이디).emit('이벤트명', 데이터); // 그룹 전체
    > socket.broadcast.to(방의 아이디).emit('이벤트명', 데이터); // 나를 제외한 그룹 전체
    > ```

  * 그룹 목록과 그룹 안의 소켓들을 확인하는 법

    > ```Javascript
    > io.adapter.rooms
    > io.of(네임스페이스).adapter.rooms
    > socket.adapter.rooms
    > ```

    * but 위의 방법대로 하면 인원 수나 방의 수를 구하는 것이 불안전하기 때문에, 서버상에서 배열을 만들어 받은 아이디를 모아두는 것이 편할 것 (방 안에는 참여한 사람들의 소켓 아이디를 넣어두고 ~)

      > ```Javascript
      > [
      >     { _id: 'room01', members: ['zero_id', 'aero_id']},
      >     { _id: 'room02', members: ['nero_id', 'hero_id']},
      > ]
      > ```

      * 이런 식으로 저장할 경우 서버가 꺼지지 않는 이상 저 배열은 데이터베이스처럼 동작함.



## 간단한 채팅 프로그램

#### Namespace 사용하지 않는 채팅 프로그램

* app.js(Server)

  > ```Javascript
  > var app = require('express')();
  > var server = require('http').createServer(app);
  > // http server를 socket.io server로 upgrade한다
  > var io = require('socket.io')(server);
  > // localhost:3000으로 서버에 접속하면 클라이언트로 index.html을 전송한다
  > app.get('/', function(req, res) {
  >     res.sendFile(__dirname + '/index.html');
  > });
  > // connection event handler
  > // connection이 수립되면 event handler function의 인자로 socket인 들어온다
  > io.on('connection', function(socket) {
  >     // 접속한 클라이언트의 정보가 수신되면
  >     socket.on('login', function(data) {
  >         console.log('Client logged-in:\n name:' + data.name + '\n userid: ' + data.userid);
  >         // socket에 클라이언트 정보를 저장한다
  >         socket.name = data.name;
  >         socket.userid = data.userid;
  >         // 접속된 모든 클라이언트에게 메시지를 전송한다
  >         io.emit('login', data.name );
  >     });
  >     // 클라이언트로부터의 메시지가 수신되면
  >     socket.on('chat', function(data) {
  >         console.log('Message from %s: %s', socket.name, data.msg);
  >         var msg = {
  >             from: {
  >                 name: socket.name,
  >                 userid: socket.userid
  >             },
  >             msg: data.msg
  >         };
  >         // 메시지를 전송한 클라이언트를 제외한 모든 클라이언트에게 메시지를 전송한다
  >         //socket.broadcast.emit('chat', msg);
  >         // 메시지를 전송한 클라이언트에게만 메시지를 전송한다
  >         // socket.emit('s2c chat', msg);
  >         // 접속된 모든 클라이언트에게 메시지를 전송한다
  >         io.emit('chat', msg);
  >         // 특정 클라이언트에게만 메시지를 전송한다
  >         // io.to(id).emit('s2c chat', data);
  >     });
  >     // force client disconnect from server
  >     socket.on('forceDisconnect', function() {
  >         socket.disconnect();
  >     })
  >     socket.on('disconnect', function() {
  >         console.log('user disconnected: ' + socket.name);
  >     });
  > });
  > server.listen(3000, function() {
  >     console.log('Socket IO server listening on port 3000');
  > });
  > ```

* Index.html(Client)

  > ```HTML
  > <!DOCTYPE html>
  > <html>
  >     <head>
  >         <meta charset="utf-8">
  >         <title>Socket.io Chat Example</title>
  >         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  >     </head>
  >     <body>
  >         <div class="container">
  >             <h3>Socket.io Chat Example</h3>
  >             <form class="form-inline">
  >                 <div class="form-group">
  >                     <label for="msgForm">Message: </label>
  >                     <input type="text" class="form-control" id="msgForm">
  >                 </div>
  >                 <button type="submit" class="btn btn-primary">Send</button>
  >             </form>
  >             <div id="chatLogs"></div>
  >         </div>
  >         <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
  >         <script src="/socket.io/socket.io.js"></script>
  >         <script>
  >             $(function(){
  >                 // socket.io 서버에 접속한다
  >                 var socket = io();
  >                 // 서버로 자신의 정보를 전송한다.
  >                 socket.emit("login", {
  >                     // name: "ungmo2",
  >                     name: makeRandomName(),
  >                     userid: "ungmo2@gmail.com"
  >                 });
  >                 // 서버로부터의 메시지가 수신되면
  >                 socket.on("login", function(data) {
  >                     $("#chatLogs").append("<div><strong>" + data + "</strong> has joined</div>");
  >                 });
  >                 // 서버로부터의 메시지가 수신되면
  >                 socket.on("chat", function(data) {
  >                     $("#chatLogs").append("<div>" + data.msg + " : from <strong>" + data.from.name + "</strong></div>");
  >                 });
  >                 // Send 버튼이 클릭되면
  >                 $("form").submit(function(e) {
  >                     e.preventDefault();
  >                     var $msgForm = $("#msgForm");
  >                     // 서버로 메시지를 전송한다.
  >                     socket.emit("chat", { msg: $msgForm.val() });
  >                     $msgForm.val("");
  >                 });
  >                 function makeRandomName(){
  >                     var name = "";
  >                     var possible = "abcdefghijklmnopqrstuvwxyz";
  >                     for( var i = 0; i < 3; i++ ) {
  >                         name += possible.charAt(Math.floor(Math.random() * possible.length));
  >                     }
  >                     return name;
  >                 }
  >             });
  >         </script>
  >     </body>
  > </html>
  > ```



#### Namespace사용하는 채팅 프로그램

* app.js(Server)

  > ```Javascript
  > var app = require('express')();
  > var server = require('http').createServer(app);
  > // http server를 socket.io server로 upgrade한다
  > var io = require('socket.io')(server);
  > // localhost:3000으로 서버에 접속하면 클라이언트로 index.html을 전송한다
  > app.get('/', function(req, res) {
  >     res.sendFile(__dirname + '/index-room.html');
  > });
  > // namespace /chat에 접속한다.
  > var chat = io.of('/chat').on('connection', function(socket) {
  >     socket.on('chat message', function(data){
  >         console.log('message from client: ', data);
  >         var name = socket.name = data.name;
  >         var room = socket.room = data.room;
  >         // room에 join한다
  >         socket.join(room);
  >         // room에 join되어 있는 클라이언트에게 메시지를 전송한다
  >         chat.to(room).emit('chat message', data.msg);
  >     });
  > });
  > server.listen(3000, function() {
  >     console.log('Socket IO server listening on port 3000');
  > });
  > ```

* index.html(Client)

  > ```html
  > <!DOCTYPE html>
  > <html>
  >     <head>
  >         <meta charset="utf-8">
  >         <title>Socket.io Chat Example</title>
  >         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  >     </head>
  >     <body>
  >         <div class="container">
  >             <h3>Socket.io Chat Example</h3>
  >             <!-- <form class="form-inline"> -->
  >             <form class="form-horizontal">
  >                 <div class="form-group">
  >                     <label for="name" class="col-sm-2 control-label">Name</label>
  >                     <div class="col-sm-10">
  >                         <input type="text" class="form-control" id="name" placeholder="Name">
  >                     </div>
  >                 </div>
  >                 <div class="form-group">
  >                     <label for="room" class="col-sm-2 control-label">Room</label>
  >                     <div class="col-sm-10">
  >                         <input type="text" class="form-control" id="room" placeholder="Room">
  >                     </div>
  >                 </div>
  >                 <div class="form-group">
  >                     <label for="msg" class="col-sm-2 control-label">Message</label>
  >                     <div class="col-sm-10">
  >                         <input type="text" class="form-control" id="msg" placeholder="Message">
  >                     </div>
  >                 </div>
  >                 <div class="form-group">
  >                     <div class="col-sm-offset-2 col-sm-10">
  >                         <button type="submit" class="btn btn-default">Send</button>
  >                     </div>
  >                 </div>
  >             </form>
  >             <ul id="chat"></ul>
  >         </div>
  >         <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
  >         <script src="/socket.io/socket.io.js"></script>
  >         <script>
  >             $(function() {
  >                 // 지정 namespace로 접속한다
  >                 var chat = io('http://localhost:3000/chat'),
  >                     news = io('/news');
  >                 $("form").submit(function(e) {
  >                     e.preventDefault();
  >                     // 서버로 자신의 정보를 전송한다.
  >                     chat.emit("chat message", {
  >                         name: $("#name").val(),
  >                         room: $("#room").val(),
  >                         msg: $("#msg").val()
  >                     });
  >                 });
  >                 // 서버로부터의 메시지가 수신되면
  >                 chat.on("chat message", function(data) {
  >                     $("#chat").append($('<li>').text(data));
  >                 });
  >             });
  >         </script>
  >     </body>
  > </html>
  > 
  > ```