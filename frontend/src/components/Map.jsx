import React, { useEffect } from 'react';
import mapboxgl from 'mapbox-gl';
import MapboxDirections from '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions';

import '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions.css';
import 'mapbox-gl/dist/mapbox-gl.css';

mapboxgl.accessToken = 'pk.eyJ1IjoiaGltZWxzYWhhMjkiLCJhIjoiY2xmMG9xdHUzMDBpYTNybzlnZTBydnlvdyJ9.jH-mX6EyYU2htEyLn8aMDw';

function Map(props) {
  useEffect(() => {
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v12',
      center: [-73.5674, 45.5019],
      zoom: 10,
    });
    var directions;
    map.addControl(
      directions = new MapboxDirections({
        accessToken: mapboxgl.accessToken,
        unit: 'metric',
        profile: 'mapbox/driving',
        controls: {
          profileSwitcher: false
        },
      }),
      'top-left'
    );

    if (props.flag == true) {
      setTimeout(() => {
        directions.setOrigin("Montréal-Pierre Elliott Trudeau International Airport (YUL), 975 rue Roméo-Vachon Nord, Dorval, Quebec H4Y 1H1, Canada");
      }, 7000);

      setTimeout(() => {
        directions.setDestination("845 Sherbrooke O Rue, Montréal, Quebec H3A 0G4, Canada");
      }, 9000);
    } else {
      setTimeout(() => {
        directions.setOrigin("845 Sherbrooke O Rue, Montréal, Quebec H3A 0G4, Canada");
      }, 7000);

      setTimeout(() => {
        alert('Destination address missing');
      }, 9000);
    }


    
    directions.on('origin', (e) => {
      console.log('Origin: ' + JSON.stringify(e.feature.geometry));
    });

    directions.on('destination', (e) => {
      console.log('Destination: ' + e.feature.geometry.coordinates);
    });

    directions.on("route", e => {
      let routes = e.route
      console.log("Route lengths", routes.map(r => r.distance)[0])
    })


    return () => {
      map.remove();
    };
  }, []);

  return (
    <div style={{ position: 'absolute', top: 0, bottom: 0, width: '100%' }}>
      <div id="map" style={{ height: '100%' }} />
    </div>
  );
};

export default Map;
