import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// this is important do not delete — https://www.youtube.com/watch?v=qi32YwjoN2U

// pages
import TitlePage from './TitlePage'
import Competitive from './Competitive'
import Practice from './Practice'
import Results from './Results'

import { HashRouter as Router, Route, Routes } from 'react-router-dom'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<TitlePage/>} />
          <Route path="/competitive" element={<Competitive />} />
          <Route path="/practice" element={<Practice />} />
          <Route path="/results" element={<Results />} />
          {/* Add more routes as needed */}
        </Routes>
      </Router>
    </>
  )
}

export default App
