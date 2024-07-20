import React, { useState } from 'react';
import axios from 'axios';
import  './guess.css'

function Guess() {
  const [symbol, setSymbol] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [forecast, setForecast] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/guess', {
        symbol,
        start_date: startDate,
        end_date: endDate
      });
      setForecast(response.data);
      setError('');
    } catch (err) {
      setError('Error fetching forecast. Please check your inputs.');
      setForecast(null);
    }
  };

  return (
    <div className="container">
      <h1>Stock Price Forecast</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Symbol:</label>
          <input
            type="text"
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Start Date:</label>
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>End Date:</label>
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            required
          />
        </div>
        <button type="submit">Get Forecast</button>
      </form>
      {error && <p className="error">{error}</p>}
      {forecast && (
        <div className="forecast">
          <h2>Forecast Results:</h2>
          <pre>{JSON.stringify(forecast, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default Guess;
