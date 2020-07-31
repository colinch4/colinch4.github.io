## URL 주소 분석

> ```javascript
> var app = http.createServer(function (request, response) {
>     //전체 url 저장
>     var _url = request.url;
>     //url의 queryData 저장
>     var queryData = url.parse(_url, true).query;
>     //url의 경로 저장
>     var pathname = url.parse(_url, true).pathname;
> }
> ```

