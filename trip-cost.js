const tripID_label = document.getElementById("trip-id");
const price_label = document.getElementById("price");
const num_passengers_label = document.getElementById("num_passengers");
const price_pp_label = document.getElementById("price_pp");
const trip_length_label = document.getElementById("trip_length");
const fuel_cons_label = document.getElementById("fuel_cons");
const emissions_saved_label = document.getElementById("emissions_saved");

console.log(tripID_label)

//pendulum color

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function updateTripValues() {
    //here instead of calling random Int call the backend
    let tripID = getRandomInt(100000)
    let price = getRandomInt(100)+10
    let num_passengers = getRandomInt(4)
    let tripLength = getRandomInt(100)+5
    let fuelPerKM = getRandomInt(0.5)+0.1
    let emissionsPerFuel = getRandomInt(100)+10
    let fuelCons = fuelPerKM * tripLength
    let price_pp = price / num_passengers
    if (num_passengers == 0) {
        price_pp = "N/A"
    }
    let emissionsSaved = (num_passengers) * fuelCons * emissionsPerFuel
    tripID_label.innerText = "Trip ID: " + tripID
    price_label.innerText = "Total cost (CAD): " + price
    num_passengers_label.innerText = "Num passengers (not including driver): " + num_passengers
    price_pp_label.innerText = "Cost per passenger (CAD): " + price_pp
    trip_length_label.innerText = "Trip length (km): " + tripLength
    fuel_cons_label.innerText = "Estimated fuel consumption (L): " + fuelCons
    emissions_saved_label.innerText = "Estimated C02 emission saved (kg of CO2): " + emissionsSaved
}


updateTripValues()