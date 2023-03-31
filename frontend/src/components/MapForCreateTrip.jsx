import React, { useEffect } from 'react';
import mapboxgl from 'mapbox-gl';
import MapboxDirections from '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions';

import '@mapbox/mapbox-gl-directions/dist/mapbox-gl-directions.css';
import 'mapbox-gl/dist/mapbox-gl.css';

mapboxgl.accessToken = 'pk.eyJ1IjoiaGltZWxzYWhhMjkiLCJhIjoiY2xmMG9xdHUzMDBpYTNybzlnZTBydnlvdyJ9.jH-mX6EyYU2htEyLn8aMDw';

function MapForCreateTrip(props) {

  const { selectedPickup, setPickup, selectedDropoff, setDropoff, isLoading, setLoading, addresses, setAddresses, pick_up_address_line_1, pick_up_city, pick_up_postal_code, drop_off_postal_code, drop_off_city, drop_off_address_line_1, distance_km } = props;
  useEffect(() => {
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v12',
      center: [-73.5674, 45.5019],
      zoom: 9,
    });
    var directions;
    map.addControl(
      directions = new MapboxDirections({
        accessToken: mapboxgl.accessToken,
        unit: 'metric',
        profile: 'mapbox/driving',
        controls: {
          profileSwitcher: false
        }
      }),
      'top-left'
    );

    directions.on('origin', (e) => {
      console.log('Origin: ' + JSON.stringify(e.feature.geometry.coordinates));
      //console.log(e.feature.geometry.coordinates[1]);
      const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${e.feature.geometry.coordinates[0]},${e.feature.geometry.coordinates[1]}.json`;
      const params = {
        access_token: mapboxgl.accessToken
      };
      fetch(url + '?' + new URLSearchParams(params))
        .then(response => response.json())
        .then(data => {
          var location = data.features[0].place_name;
          console.log('pickup_location:', location);
          localStorage.setItem('pickup_location', location);
          setPickup("Create New");
          location = location.split(',');
          props.pick_up_address_line_1.current.value = location[0];
          props.pick_up_city.current.value = location[1];
          props.pick_up_postal_code.current.value = location[2];
        });

    });

    directions.on('destination', (e) => {
      console.log('Destination: ' + e.feature.geometry.coordinates);
      //console.log(e.feature.geometry.coordinates[1]);
      const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${e.feature.geometry.coordinates[0]},${e.feature.geometry.coordinates[1]}.json`;
      const params = {
        access_token: mapboxgl.accessToken
      };
      fetch(url + '?' + new URLSearchParams(params))
        .then(response => response.json())
        .then(data => {
          var location = data.features[0].place_name;
          console.log('dropoff_location:', location);
          localStorage.setItem('dropoff_location', location);
          setDropoff("Create New");
          location = location.split(',');
          props.drop_off_address_line_1.current.value = location[0];
          props.drop_off_city.current.value = location[1];
          props.drop_off_postal_code.current.value = location[2];
          
        });
    });

    directions.on("route", e => {
      let routes = e.route
      console.log("Route lengths", routes.map(r => r.distance)[0]);
      props.distance_km.current.value = (routes.map(r => r.distance)[0]).toString() + " m";
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

export default MapForCreateTrip;
