import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [dailyGoal, setDailyGoal] = useState(null);

  useEffect(() => {
    fetchDailyGoal();
  }, []);

  const fetchDailyGoal = async () => {
    try {
      const response = await fetch('/api/daily-goal');
      const data = await response.json();
      setDailyGoal(data);
    } catch (error) {
      console.error('Error fetching daily goal:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>LiveLifeCooler</h1>
        {dailyGoal ? (
          <>
            <h2>Daily Goal: {dailyGoal.goal}</h2>
            <img src={dailyGoal.image_url} alt="Daily goal illustration" />
            <p>Date: {dailyGoal.date}</p>
          </>
        ) : (
          <p>Loading daily goal...</p>
        )}
      </header>
    </div>
  );
}

export default App;
