import React, { useState, useEffect } from 'react';
import Map from '../MapDisplay';
import { Link, useLocation } from 'react-router-dom';

const ViewTripsAsDriverMap = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  
  const [pickupAddress, setPickupAddress] = useState('');
  const [dropoffAddress, setDropoffAddress] = useState('');

  useEffect(() => {
    const pickup = queryParams.get('pickupAddress');
    const dropoff = queryParams.get('dropoffAddress');
    if (pickup) {
      setPickupAddress(pickup);
    }
    if (dropoff) {
      setDropoffAddress(dropoff);
    }
  }, [queryParams]);

  return (
    <div>
      <div className="box" style={{width:"800px", height:"700px", border: "1px solid black", right:"550px", position:"absolute", top:"100px"}}>
        <Map pickupLocation={pickupAddress} dropoffLocation={dropoffAddress} />
      </div>
      <Link to="/view-trips-as-driver" style={{ position: 'absolute', top: '20px', right: '20px' }}>
        <button>Return</button>
      </Link>
    </div>
  );
};

export default ViewTripsAsDriverMap;