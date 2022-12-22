from flight_map import FlightMap as FM
fm = FM()
fm.import_airports("aeroports.csv")
fm.import_flights("flights.csv")

fm.airports()
fm.flights()
