import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { Plans } from './Plans.js'
import { EnterZipCodeForm } from './EnterZipCodeForm.js'

function App() {

  const [plans, setPlans] = useState([]);

  // Fetch plan data from Flask API then set the state
  useEffect(() => {
    fetch('/75487').then(res =>
        res.json().then(data => {
        //console.log("this is data:" + data)
            setPlans(data);
        })
    );
  }, []);


  return <div className="App">

      <Plans plans={plans} />
      <EnterZipCodeForm />
  </div>;
}

export default App;