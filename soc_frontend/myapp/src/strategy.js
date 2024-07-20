import React, { useState } from 'react';
import axios from 'axios';
import { UnControlled as CodeMirror } from 'react-codemirror2';
import 'codemirror/lib/codemirror.css';
import 'codemirror/theme/material.css';
import 'codemirror/mode/python/python';
import { useNavigate } from 'react-router-dom';

function Strategy() {
  const [symbol, setSymbol] = useState('');
  const [start_date, setStartDate] = useState('');
  const [end_date, setEndDate] = useState('');
  const [stockData, setStockData] = useState([]);
  const [output, setOutput] = useState('');
  const [errors, setErrors] = useState('');
  const [script, setScript] = useState(`# Example Strategy Script
import pandas as pd
import sys

# Read the input from stdin
data = pd.read_csv(sys.stdin)

# Calculate the 10-period simple moving average
data['SMA'] = data['Close'].rolling(window=10).mean()

# Generate buy and sell signals
data['signal'] = 0
data.loc[data['Close'] > data['SMA'], 'signal'] = 1  # Buy signal
data.loc[data['Close'] < data['SMA'], 'signal'] = -1  # Sell signal

# Print the results
print(data[['Date','Open', 'Close', 'SMA', 'signal']].tail())`);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/get_stock_data', {
        symbol,
        start_date,
        end_date
      });
      console.log(response.data);
      setStockData(response.data);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };

  const handleRun = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/run_strategy', {
        script,
        stock_data: stockData
      });
      console.log("Response from backend:", response.data); // Log the backend response
      setOutput(response.data.output || 'No output');
      setErrors(response.data.errors || 'No errors');
    } catch (error) {
      console.error('Error running strategy:', error);
      setErrors('Error running strategy: ' + error.message);
    }
  };
  

  return (
    <div>
      <form onSubmit={handleSubmit} className="container mt-4">
        <div className="form-row align-items-center">
          <div className="col-auto">
            <label className="sr-only" htmlFor="symbolInput">
              Symbol
            </label>
            <input
              type="text"
              className="form-control mb-2"
              id="symbolInput"
              placeholder="Symbol"
              value={symbol}
              onChange={(e) => setSymbol(e.target.value)}
            />
          </div>
          <div className="col-auto">
            <label className="sr-only" htmlFor="startDateInput">
              Start Date
            </label>
            <input
              type="date"
              className="form-control mb-2"
              id="startDateInput"
              value={start_date}
              onChange={(e) => setStartDate(e.target.value)}
            />
          </div>
          <div className="col-auto">
            <label className="sr-only" htmlFor="endDateInput">
              End Date
            </label>
            <input
              type="date"
              className="form-control mb-2"
              id="endDateInput"
              value={end_date}
              onChange={(e) => setEndDate(e.target.value)}
            />
          </div>
          <div className="col-auto">
            <button type="submit" className="btn btn-primary mb-2">
              Preprocess
            </button>
          </div>
        </div>
      </form>
      <br />
      <div>
        <h3>Strategy Editor</h3>
        <CodeMirror
          value={script}
          options={{
            mode: 'python',
            theme: 'material',
            lineNumbers: true
          }}
          onChange={(editor, data, value) => {
            setScript(value);
          }}
        />
        <button onClick={handleRun} className="btn btn-success mt-2">
          Run Strategy
        </button>
      </div>
      <br />
      <h3>Results:</h3>
      <pre>{output}</pre>
    </div>
  );
}

export default Strategy;

