import { useEffect, useState } from 'react'
import './App.css'

function App() {


  const [events, setEvents] = useState([])


  useEffect(() => {
    const fetchEvents = async () => {
        try {
            const response = await fetch('/api/events');
            if (!response.ok) {
                throw new Error('Failed to fetch events');
            }
            const data = await response.json();
            setEvents(data);
        } catch (error) {
            console.error('Error fetching events:', error.message);
        }
    };

    fetchEvents();
}, []);


  console.log(events)
  return (
    <>
      <h1>Let's do</h1>
    </>
  )
}

export default App
