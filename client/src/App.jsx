import { useEffect, useState } from 'react'
// import './App.css'
import Navbar from './components/Navbar';
import { Outlet } from 'react-router-dom';


function App() {

  const [events, setEvents] = useState()

  useEffect(() => {

    const fetchEvents = async () => {

      try {

        const response = await fetch("/api/events")
        const data = await response.json()

        if (!response.ok) {
          // console.log(response.error.message)
          console.log("Response is sick")
        }
        setEvents(data)
        
      } catch (error) {
        console.error("Writing bad")
      }

     
    }

    fetchEvents()
  }, [])
  
  return (
    <>

      <Navbar />
      <Outlet context = {{ events }} />
    </>
  )
}

export default App
