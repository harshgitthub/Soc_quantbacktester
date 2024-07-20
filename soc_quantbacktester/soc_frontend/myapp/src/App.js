
import './App.css';

import React, { useState } from 'react';

import StockForm from './form';
import { BrowserRouter as Router, Routes, Route, Switch, Link, BrowserRouter } from 'react-router-dom';

import Trend from './trend';
import PostTrade from './post_trade';
import Strategy from './strategy';
import Guess from './guess';


function App() {
  const [data, setData] = useState(null);

  

  return (
    
    <BrowserRouter>
    <div className="App">
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <a className="navbar-brand" href="/">Stocker</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/">Show Data</a>
        </li>
        <li className="nav-item">
          <a className="nav-link active" href="/strategy">Strategy</a>
        </li>
        
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/post">Analysis</a>
        </li>
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="/guess">Guess</a>
        </li>

        <li className="nav-item"><a className="nav-link active" target='_blank' aria-current="page" href="https://in.tradingview.com/">Trading view</a></li>
        <li className="nav-item"><a className="nav-link active" target='_blank'  aria-current="page" href="https://www.chittorgarh.com/">Chittorgarh.com</a></li>
            <li className="nav-item"><a className="nav-link active" target='_blank'  aria-current="page" href="https://intradayscreener.com/stock-market-today">Intraday screener</a></li>
            <li className="nav-item"> <a className="nav-link active" target='_blank'  aria-current="page" href="https://www.moneycontrol.com/">Moneycontrol</a></li>
      </ul>

     
    </div>
    
  </div>
</nav>
    <header className="App-header"></header>
    <Routes>
    <Route path="/" element={<StockForm/>} />
    <Route path='/post' element={<PostTrade/>}/>
   
    <Route path='/guess' element={<Guess/>}/>
    <Route path="/trend" element={<Trend/>} />
    <Route path='/strategy' element={<Strategy/>}/>   
     {/* <Route path="/data-input" element={<DataInput/>} />
        <Route path="/preprocess" element={<Preprocess/>
        } />
        <Route path="/strategy-editor" element={<StrategyEditor/>} />
        <Route path="/result-display" element={<ResultDisplay/>} /> */}
    {/* </Route> */}
    </Routes>

      {/* <StockForm/> */}
  </div>
  </BrowserRouter>
  );
}


export default App;
