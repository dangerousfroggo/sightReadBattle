import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  return (
    <>
      <h1>
        Clef Clash
      </h1>
      <div className="gamemode-buttons-container"> {/* this contains the buttons of casual, competitive, and practice */}
        <button onClick={() => setCount((count) => count + 1)}>
          Casual
          {/*<img src={viteLogo} className="logo vite" alt="Vite logo" />*/}
        </button>
        <button onClick={() => setCount((count) => count + 1)}>
          Competitive
        </button>
        <button onClick={() => setCount((count) => count + 1)}>
          Practice
        </button>
      </div>
      <div className="options-buttons-container"> {/* this contains the buttons of options, settings, and profile */}
        <button className="options" onClick={() => setCount((count) => count + 1)}>
          Options
        </button>
        <button className="options" onClick={() => setCount((count) => count + 1)}>
          Settings
        </button>
        <button className="options" onClick={() => setCount((count) => count + 1)}>
          Profile
        </button>
      </div>
    </>
  )
}

export default App
