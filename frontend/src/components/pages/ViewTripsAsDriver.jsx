import React from 'react';

const ViewTripsCreatedAsDriver = () => {
  const driverTrips = [
    {
      id: 1,
      pickup: "123 Main St.",
      dropoff: "456 Elm St.",
      date: "2023-03-20",
      time: "10:00 AM",
      fare: 25.00,
      availableSeats: 2,
      passengers: [
        {
          name: "John Doe",
          pickup: "123 Main St.",
          dropoff: "456 Elm St.",
          contact: "john.doe@example.com"
        },
        {
          name: "Jane Smith",
          pickup: "789 Oak St.",
          dropoff: "123 Main St.",
          contact: "jane.smith@example.com"
        }
      ]
    },
    // add more trips here as needed
  ];

  return (
    <div>
      <h1>Trips Created</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Pickup</th>
            <th>Dropoff</th>
            <th>Date</th>
            <th>Time</th>
            <th>Fare</th>
            <th>Available Seats</th>
            <th>Passengers</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {driverTrips.map(trip => (
            <tr key={trip.id}>
              <td>{trip.id}</td>
              <td>{trip.pickup}</td>
              <td>{trip.dropoff}</td>
              <td>{trip.date}</td>
              <td>{trip.time}</td>
              <td>${trip.fare.toFixed(2)}</td>
              <td>{trip.availableSeats}</td>
              <td>
                <ul>
                  {trip.passengers.map(passenger => (
                    <li key={passenger.contact}>
                      {passenger.name} ({passenger.pickup} to {passenger.dropoff})
                    </li>
                  ))}
                </ul>
              </td>
              <td>
                <button>Edit</button>
                <button>Cancel</button>
                <button>Map</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <style jsx>{`
        table {
          width: 100%;
          margin: 10px auto;
          border-collapse: collapse;
        }
        
        th, td {
          padding: 8px;
          text-align: left;
          border-bottom: 1px solid #ddd;
        }
        
        tr:nth-child(even) {
          background-color: #f2f2f2;
        }
        
        tr:hover {
          background-color: #ddd;
        }
        
        .container {
          padding: 10px;
          border: 1px solid #ccc;
        }
      `}</style>
    </div>
  );
};

export default ViewTripsCreatedAsDriver;