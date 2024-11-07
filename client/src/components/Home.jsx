import React from 'react';

const Home = () => {
  const events = [
    {
      id: 1,
      title: 'Art & Design Workshop',
      date: 'Nov 15, 2024',
      location: 'Downtown Art Center',
      description: 'Explore your creativity in our hands-on art workshop.',
    },
    {
      id: 2,
      title: 'Tech Conference 2024',
      date: 'Dec 2, 2024',
      location: 'TechHub Convention Center',
      description: 'Join industry leaders in discussing the future of technology.',
    },
    // Add more event objects as needed
  ];

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-4xl font-bold text-center mb-8">Available Events</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {events.map((event) => (
          <div key={event.id} className="bg-white shadow-lg rounded-lg p-4 border hover:shadow-xl transition-shadow">
            <h2 className="text-2xl font-semibold text-gray-800 mb-2">{event.title}</h2>
            <p className="text-gray-600 mb-1"><strong>Date:</strong> {event.date}</p>
            <p className="text-gray-600 mb-1"><strong>Location:</strong> {event.location}</p>
            <p className="text-gray-700">{event.description}</p>
            <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
              Learn More
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
