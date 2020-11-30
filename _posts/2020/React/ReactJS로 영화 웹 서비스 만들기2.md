# ReactJS로 영화 웹 서비스 만들기 💻 

## 2️⃣
### 🖥 MAKING THE MOVIE APP - 4
#### 4 - 0. Fetching Movies from API
- 데이터를 받아오기 위해 axios 설치 $ npm i axios 

```javascript
getMovies = async () => {
    // 데이터를 받아오기 위한 비동기 처리
    const movies = await axios.get("https://yts-proxy.now.sh/list_movies.json");
}

componentDidMount() {
    this.getMovies();
}
```

#### 4 - 1. Rendering the Movies
- 컴포넌트가 state 필요 없는경우에는 class component로 하지 않아도 된다.

```javascript
// src/App.js
getMovies = async () => {
    const {data: {data: {movies}}} = await axios.get("https://yts-proxy.now.sh/list_movies.json?sort_by=rating");
   this.setState({movies, isLoading: false})
    //  this.setState({movies(state.movies):movies(위에서 받아온 데이터의 movies)})
}

// src/Moive.js ( state 가 필요없기때문에 함수 컴포넌트를 이용)
import React from 'react';
import PropTyeps from 'prop-types';

function Movie({id, year, title, summary, poster}){
    return (
        <h4>{title}</h4>
    )
}

Movie.prototype = {
    id: PropTyeps.number.isRequired,
    year: PropTyeps.string.isRequired,
    title: PropTyeps.string.isRequired,
    summary: PropTyeps.string.isRequired ,
    poster: PropTyeps.string.isRequired
}

export default Movie;
```

#### 4 - 2. Styling the Movies
- 1. 해당컴포넌트에 해당하는 css 파일을 만들고 js 파일에 import 하는 방식으로 사용 (import './App.css';)
- 2. 태그에 style={{ backgroundColor:'red'}} 이런식으로 사용 

#### 4 - 3. Adding Genres
- jsx 형식에 class component 와 혼란을 막기 위해 태그안에 class="" -> className="" 로 변경해줘야한다.

#### 4 - 5. Cutting the summary
- 줄거리 내용이 길어서 넘칠때 <p>{summary.slice(0, 180)}...</p>

### 🖥 CONCLUSIONS - 5
#### 5 - 0. Deploying to Github Pages
- 만든 앱 페이지 배포 !
- gh-pages 를 설치한다 $ npm i gh-pages
- package.json 에 hompage를 추가한다. ( "homepage": "https://jina95.github.io/movieApp_react/" ) -> 소문자와 띄어쓰기는 안됨!
- deploy와 predeploy 명령어를 추가해준다.
- deploy 는 build 폴더를 업로드 해준다 .( build 폴더를 얻기 위해서는 $npm run build)
- deploy 를 호출하면, predeploy가 자동으로 실행된다.(이름이 같아야 함)

<img src="https://github.com/jina95/TIL/blob/master/images/react/react_deploy.png" width="50%">

#### 5 - 1. Are we done?
- state를 갖기 위해 class component를 가질 필요가 없다 ( react 의 새로운 부분..? react hook 때문이라고 함!)

### 🖥  ROUTING BONUS - 6
#### 6 - 0. Getting Ready for the Router
- $ npm i react-router-dom
- 전체적인 구조 변경 ( home <-> about )

#### 6 - 1. Building the Router

```javascript
//  src/App.js
import React from 'react';
import { HashRouter, Route  } from 'react-router-dom'
import About from './routes/About'

function App(){
  return (
    <HashRouter>
      {/* Route 안에 중요한 props 2개가 들어간다. */}
      {/* 1. 랜더링할 스크린 */}
      {/* 2. 뭘 할지 정해주는 props */}
      <Route path="/" component={Home} />
      <Route path="/about" component={About} />
      {/* 만약 내가  path="/about" 로 가게되면 component={About}을 보여줘 라는 뜻 */}
    </HashRouter>
  );
} 

export default App;
```

- 하지만 위와같은 코드에서는 /about로 들어가게되면 home , about 둘다 뜨는것을 확인할 수 있다.
- 렌더링 방식때문이라 path="/about"이 path="/" 안에 포함된다고 생각을하고 렌더링을 하기 때문
- 이때 아래와 같이 값을 추가해주면 위와 같은 상황이 안벌어진다.

```javascript
function App(){
  return (
    <HashRouter>
      <Route path="/" exact={true} component={Home} />
      {/* only url path="/" 일때만 Home 이 렌더링 되게  */}
      <Route path="/about" component={About} />
    </HashRouter>
  );
} 
```

- exact : 이거 아니면 렌더링 안한다는 뜻

#### 6 - 2. Building the Navigation

```javascript
// component/Navigation.js
import React from 'react'
import { Link } from 'react-router-dom'

function Navigation(){
    return (
      <div>
        {/* <a href="/">HOME</a>
        <a href="/about">ABOUT</a> */}
        {/* a  href 를 사용하면 페이지를 아예 새로고침해버린다. */}
        <Link to="/">HOME</Link>
        <Link to="/about">ABOUT</Link>
      </div>
    );
}

export default Navigation;

// src/App.js
function App(){
  return (
    <HashRouter>
      <Navigation />
      {/*  Navigation 안에서 사용되는 Link 는 Router 밖에서는 사용될 수 없다.*/}
      <Route path="/" exact={true} component={Home} />
      <Route path="/about" component={About} />
    </HashRouter>
  );
} 
```

#### 6 - 3. Sharing Props Between Routes
- router 에 있는 모든 router들은 props를 가진다.

```javascript
// component/Navigation.js
function Navigation(){
    return (
      <div>
        <Link to="/">HOME</Link>
        <Link to={{ 
            pathname: '/about',
            state: {
                fromNavigation: true
            }
        }}>ABOUT</Link>
        {/*  to 에는 string 을 넣을 수 있고, object를 사용할 수도 있다. */}
      </div>
    );
}

// route/About.js
function About(props){
    console.log(props);
    // location > state 에서 보낸 props 를 확인할 수 있다.
    return <span>About this page</span>
}
```

- 영화를 누르면 상세화면으로 넘어가기때문에 , Movie.js 의 div를 Link로 바꿔주고, state 의 props 값을 전달해 주었다.

```javascript
function Movie({ year, title, summary, poster, genres }) {
  return (
    <Link to={{
      pathname: '/movie-detail',
      state: {
        title, year, summary, poster, genres 
      }
    }}>
      <div className="movie">
        // ....
      </div>
    </Link>
  );
}
```

#### 6 - 4. Redirecting 
- 카드를 눌렀을때만 detail page 에 들어가야하는데 새로고침하면 받아온 값이 없어서 undefined가 뜬다 
- 이때 리다이렉트 방법!

```javascript
import React from 'react';

class Detail extends React.Component{
    componentDidMount(){
        const { location, history } = this.props;
        if(location.state === undefined){
            history.push("/")
            // 카드를 클릭해서 들어온게 아니라면 리다이렉트 시킴( 홈 화면으로 )
        }
        console.log(location.state); 
    }

    render(){
        const {location} = this.props
        if(location.state){
            return <span>{location.state.title}</span>;
        } else return null 
    }
}

export default Detail;
```
- 또한 pathname 을 /movie-detail 로 하기보다는 각 영화의 아이디 값을 부여해 줄 수 있다.

```javascript
// Movies.js
<Link to={{
      pathname: `/movie/${id}`,
      state: {
        id, title, year, summary, poster, genres 
      }
 }}>

// App.js
<Route path="/movie/:id" component={Detail} />
      {/* :id 를 통해 변수가 있음을 알려준다. */}
```

