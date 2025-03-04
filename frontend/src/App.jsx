import SignUp from './pages/SignUp';
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Todo from './pages/Todo';
import About from './pages/About';
import Login from './pages/Login';
import Error from './pages/Error';
import NavBar from './component/NavBar';
import './App.css';
function App() {

	return (
		<div className='App'>
		<BrowserRouter>
          <NavBar />
			<Routes>
				<Route path='/' element = {<Todo/>} ></Route>
				<Route path='/about' element = {<About/>} ></Route>
				<Route path='/login' element = {<Login/>} ></Route>
				<Route path='/signup' element = {<SignUp/>} ></Route>
				<Route path='*' element = {<Error/>} ></Route>
			</Routes>
		</BrowserRouter>
		</div>
		
	)	
}

export default App;