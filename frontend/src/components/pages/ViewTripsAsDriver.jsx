import React, { useState, useEffect } from 'react';

const ViewTripsCreatedAsDriver = () => {
  const driverEmail = localStorage.getItem('email');
  const [trips, setTrips] = useState([]);

  useEffect(() => {
    const fetchTrips = async () => {
      const response = await fetch(`http://localhost:5000/trips/driver/${driverEmail}`);
      const data = await response.json();
      setTrips(data);
    };
    fetchTrips();
  }, [driverEmail]);

  return (
    <div>
      <h1>Trips Created</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Pickup Address</th>
            <th>Dropoff Address</th>
            <th>Available Seats</th>
            <th>Passengers</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {trips.map((trip) => (
            <tr key={trip.trip_id}>
              <td>{trip.trip_id}</td>
              <td>{trip.pick_up_address}</td>
              <td>{trip.drop_off_address}</td>
              <td>{trip.available_seats}</td>
              <td>
                <ul>
                  {trip.passenger_names.map((passengerName) => (
                    <li key={passengerName}>{passengerName}</li>
                  ))}
                </ul>
              </td>
              <td>
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

        th,
        td {
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