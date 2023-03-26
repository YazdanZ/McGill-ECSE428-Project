import React, { useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import MapboxDirections from '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions';

import '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions.css';
import 'mapbox-gl/dist/mapbox-gl.css';

mapboxgl.accessToken = 'pk.eyJ1IjoiaGltZWxzYWhhMjkiLCJhIjoiY2xmMG9xdHUzMDBpYTNybzlnZTBydnlvdyJ9.jH-mX6EyYU2htEyLn8aMDw';

const Map = ({ pickupLocation, dropoffLocation }) => {
  const mapContainerRef = useRef(null);
  const directionsRef = useRef(null);

  useEffect(() => {
    if (pickupLocation && dropoffLocation) {
      if (!directionsRef.current) {
        const map = new mapboxgl.Map({
          container: mapContainerRef.current,
          style: 'mapbox://styles/mapbox/streets-v12',
          center: [-73.5674, 45.5019],
          zoom: 10,
        });

        directionsRef.current = new MapboxDirections({
          accessToken: mapboxgl.accessToken,
          unit: 'metric',
          profile: 'mapbox/driving',
          controls: {
            profileSwitcher: false
          }
        });

        map.addControl(directionsRef.current, 'top-left');

        directionsRef.current.on('origin', (e) => {
          console.log('Origin: ' + JSON.stringify(e.feature.geometry));
        });

        directionsRef.current.on('destination', (e) => {
          console.log('Destination: ' + e.feature.geometry.coordinates);
        });

        directionsRef.current.on("route", e => {
          let routes = e.route
          console.log("Route lengths", routes.map(r => r.distance)[0])
        })
      }

      directionsRef.current.setOrigin(pickupLocation);
      directionsRef.current.setDestination(dropoffLocation);
    }
  }, [pickupLocation, dropoffLocation]);

  return (
    <div style={{ position: 'absolute', top: 0, bottom: 0, width: '100%' }}>
      <div ref={mapContainerRef} style={{ height: '100%' }} />
    </div>
  );
};

export default Map;