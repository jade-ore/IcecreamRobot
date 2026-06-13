import './App.css'
import CherryBlossom from './assets/CherryBlossomHome.png'
import Logo from './assets/Logo.png'
import Title from './assets/BigLetters.png'
import Button from './assets/Button.png'
import Info from './assets/Info.png'

function App() {



  return (
    <div className='bg'>
      <div id='blossom-container'>
        <img id='blossom' src={CherryBlossom}></img>
      </div>
      <img id='logo' src={Logo}></img>
      <img id='title' src={Title}></img>
      <button id='button'>
        <img src={Button}></img>
      </button>
    <img src={Info} id='info'></img>
    </div>
  )
}

export default App;