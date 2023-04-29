# - Mya Thomas
# - ID: 010507144

# - C950 Data Structures and Algorithms II

# --- DELIVERY TRUCK CLASS ----------------------------------------------------------------------

# This class creates a truck object
# (Object)
# Time Complexity -> O(1)
class DeliveryTruckClass:

    def __init__(self, location, time, departure, weight, speed, mileage, truck_parcels):
        # Delivery Trucks location
        self.location = location

        # Delivery Trucks time
        self.time = time

        # Delivery Trucks departure from (WGUPS) hub time
        self.departure = departure

        # Delivery Trucks Parcel Weight
        self.weight = weight

        # Delivery Trucks speed
        self.speed = speed

        # Delivery Trucks mileage
        self.mileage = mileage

        # Delivery Trucks packages(parcels)
        self.truck_parcels = truck_parcels

    # String to display delivery truck object
    def __str__(self):
        # Will print to console:

        # Truck (current) Location
        # Trucks (current) Time
        # Trucks Departure time from hub
        # Trucks Parcel Weight
        # Trucks Speed
        # Trucks Mileage
        # Trucks Loaded Parcels

        return ('Truck Location: %s, Current time: %s, Departure: %s, Weight: %d, Speed: %d, Mileage: %.2f, '
                'Parcels: %s ' %
                (self.location, self.time, self.departure, self.weight, self.speed, self.mileage, self.truck_parcels))
