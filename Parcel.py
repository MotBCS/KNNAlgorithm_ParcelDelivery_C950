# - Mya Thomas
# - ID: 010507144

# - C950 Data Structures and Algorithms II
# ----------------------------------------------------------------------------------------------------------------------

# Imports
import datetime


# --- PARCEL CLASS ----------------------------------------------------------------------
# Constrictor with all parcel attributes
# This class creates a parcel object
# (Object)
# Time Complexity -> O(1)
class ParcelClass:

    def __init__(self, parcel_id, address, city, state, postalCode, deadline, weight, status):
        self.parcel_id = parcel_id
        self.address = address
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.deliveryTruck_Departure = None
        self.delivery_time = None

    # String to display parcel object
    def __str__(self):
        return (' '
                '- Parcel ID:           %d\n '
                '- Parcel Address:      %s\n '
                '- Parcel City:         %s\n '
                '- Parcel State:        %s\n '
                '- Postal Code:         %s\n\n '
                '- Deliver By: %s,  Parcel Weight: %.2f,  Parcel Status: %s' %
                (self.parcel_id, self.address, self.city, self.state, self.postalCode, self.deadline, self.weight,
                 self.status))

    # --- PARCEL STATUS ----------------------------------------------------------------------

    # Return the status (position) of parcel
    # - At WGUPS Hub
    # - Out For Delivery
    # - Parcel Delivered at: (Time)

    def ReturnParcelPosition(self, input_time):
        Parcel_Status = 'At WGUPS hub'
        deliveryTruck_Departure = self.deliveryTruck_Departure
        (hours, minutes, seconds) = deliveryTruck_Departure.split(':')
        Time_format = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        # Conditional statement to determine the parcel's status
        # Parcel at Hub
        if input_time < Time_format:
            Parcel_Status = 'At WGUPS hub'

        # Conditional statement to determine the parcel's status
        # Parcel Out For Delivery
        elif input_time >= Time_format:
            if input_time < self.delivery_time:
                Parcel_Status = 'Out For Delivery'

        # Conditional statement to determine the parcel's status
        # Parcel Delivered
            else:
                Parcel_Status = 'Parcel Delivered at %s **' % self.delivery_time

        # Return string with parcel id, departure time, parcel status
        return '[ Parcel Id: %d  |   Departure: %s  |    Parcel Status: %s ]' % \
               (self.parcel_id, self.deliveryTruck_Departure, Parcel_Status)
