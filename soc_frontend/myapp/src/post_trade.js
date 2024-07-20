

import React, { useState } from 'react';
import axios from 'axios';
import './App.css'
import { Line } from 'react-chartjs-2';



function PostTrade() {
  const [symbol, setSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [data, setData] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/post_trade_analysis', {
        symbol,
        start_date: startDate,
        end_date: endDate
      });

      let responseData = response.data;

      // Normalize data to always be an array
      if (!Array.isArray(responseData)) {
        responseData = [responseData]; // Wrap the data in an array if it's not already
      }

      console.log(responseData); // Log the normalized response data
      setData(responseData);
    } catch (error) {
      console.error('There was an error fetching the data!', error);
    }
  };

  const createChartData = (label, dataSet, dataKey, color) => {
    if (!Array.isArray(dataSet)) {
      console.error('Expected dataSet to be an array, but got:', dataSet);
      return {};
    }
    return {
      labels: dataSet.map(row => {
        // Assuming `row.Date` is a date string like "2024-07-20"
        const date = new Date(row.Date); // Parse the date string into a Date object
        const formattedDate = `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`;
        return formattedDate || 'Unknown Date';
      }),
      datasets: [
        {
          label: label,
          data: dataSet.map(row => row[dataKey]),
          borderColor: color,
          fill: false,
        },
      ],
    };
  };

  return (
    <div>

      <form onSubmit={handleSubmit} className="container mt-4">
        <div className="form-row align-items-center">
          <div className="col-auto">
            <label className="sr-only" htmlFor="symbolInput">Symbol</label>
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
            <label className="sr-only" htmlFor="startDateInput">Start Date</label>
            <input 
              type="date" 
              className="form-control mb-2" 
              id="startDateInput" 
              value={startDate} 
              onChange={(e) => setStartDate(e.target.value)} 
            />
          </div>
          <div className="col-auto">
            <label className="sr-only" htmlFor="endDateInput">End Date</label>
            <input 
              type="date" 
              className="form-control mb-2" 
              id="endDateInput" 
              value={endDate} 
              onChange={(e) => setEndDate(e.target.value)} 
            />
          </div>
          <div className="col-auto">
            <button type="submit" className="btn btn-primary mb-2">Fetch Data</button>
          </div>
        </div>
      </form>

      <br/>
      {data.length > 0 && (
        
        <table className='table'>
          <thead>
            <tr>
              <th>Date</th>
            
              <th>sharpe</th>
              <th>sortino</th>
              <th>max_drawdown</th>
              <th>Volume</th>
              <th> monthly return</th>
              <th>RSI</th>
              <th> net cumulative return </th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              
              <tr key={index}>
                <td>{row.Date}</td>
               
                <td>{row.sharpe_ratio}</td>
                <td>{row.sortino_ratio}</td>
                <td>{row.max_drawdown}</td>
                <td>{row.Volume}</td>
                <td>{row.Monthly_Return}</td>
                <td>{row.RSI}</td>
                <td>{row.cumulative_return}</td>
              </tr>
              
            ))}
          </tbody>
        </table>)
}

      {data.length > 0 && (
        <Line
          data={createChartData('Cumulative Returns', data, 'cumulative_returns', 'rgb(0, 217, 255)')}
        />
      )}

      {data.length > 0 && (
        <Line
          data={createChartData('Monthly Returns', data, 'Monthly_Return', 'rgb(255, 0, 0)')}
        />
      )}

      
    </div>
  );
}

export default PostTrade;
