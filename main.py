# - Mya Thomas
# - ID: 010507144

# - C950 Data Structures and Algorithms II
# ----------------------------------------------------------------------------------------------------------------------

# Import CreateHashTable from HashTable
import HashTable

# Import DeliveryTruckClass from DeliveryTruckClass
import DeliveryTruckClass

# Import read_parcel_csv from Read_csvFile
import Read_csvFile

# Import dateTime
import datetime

print("- Mya Thomas")
print("- ID: 010507144")
print("- C950 Data Structures and Algorithms II")


# ASSUMPTIONS:
# (Reminder)
#   -   Each delivery truck can carry a maximum of 16 parcels total

#   -   ID number is unique for each parcel

#   -   No Collisions

#   -   Trucks leave WGUPS Hub only at 08:00:00 AM, with the truck loaded
#       trucks can return to hub for parcels if needed

#   -   Time factored into average speed of the trucks

#   -   Parcel 9 is delayed (Wrong Address, corrected at 10:20:00 AM)
#       Correct Address: (410 S St., Salt Lake City, UT, 84111)

#   -   Day ends after all 40 parcel have been successfully delivered

# Algorithm used: KNN (Nearest Neighbor Algorithm)


# --- USER INTERFACE -----------------------------------------------------------------------------------------------
# This section displays the main user interface, where the user can select
# between three options.
# - Option 1 allows the user to view a single parcels information
# - the user must enter a number between 1 - 40 this is the parcels
# - unique ID number and will be used to retrieve the specific
# - parcels information

# - Option 2 allows the user to view all parcel status by a certain
# - time. The user must enter their desired time in the format
# - (HH:MM:SS) Hours, minutes, and seconds
# - The user will now be able to view the parcels associated id number
# - along with delivery trucks departure time and the parcel's status
# - the status should be one of the following, 'At WGUPS Hub', 'Out For Delivery' or
# - 'Parcel Delivered at (HH:MM:SS)'

# - Option 3 allows the user to simply exit (terminate) the program
def UI(delivery_truck1,
       delivery_truck2,
       delivery_truck3,
       hash_table
       ):
    # This variable will be used to store the user input when selecting
    # a navigation option. This variable is initially set to "" (nothing)
    # until it receives an input from the user
    userChoice = ""

    # Print total mileage for all delivery trucks combined
    total_miles = delivery_truck1.mileage + delivery_truck2.mileage + delivery_truck3.mileage

    # While userChoice does not equal 3 (Exit program)
    # load welcome header and options
    while userChoice != 3:

        # Welcome Header
        print("-" * 100)
        print("---------------------------------- WGUPS PARCEL DELIVERY TRACKING ----------------------------------\n")

        print('* Total Delivery Truck Mileage: %.1f miles' % total_miles)
        print('Truck Mileage Breakdown:\n'
              ' - Delivery Truck 1: %.1f miles\n' % delivery_truck1.mileage,
              '- Delivery Truck 2: %.1f miles\n' % delivery_truck2.mileage,
              '- Delivery Truck 3: %.1f miles' % delivery_truck3.mileage)

        print('-----------------------------------------------\n')
        print('* Please Select From The Following Options Below')
        print('-----------------------------------------------\n')
        print('* (Enter) 1: To View A Specific Parcel [1-40]\n')
        print('* (Enter) 2: To View All Parcels By Time\n')
        print('* (Enter) 3: Exit Program\n')
        print("-" * 100)

        userChoice = int(input())

        # --- USER CHOICE == 1 -----------------------------------------------------------------------------------------------

        # When the user enters '1' as their choice, they will
        # receive a prompt asking them to enter
        # a parcel number to view a specific parcel
        if userChoice == 1:
            print('Enter a Parcel ID number 1-40')

            # Store user input in variable called 'userChoice'
            userChoice = int(input())

            # If user enters a number greater than 40
            # they will receive an error informing them
            # that a parcel with that id does not exist
            if userChoice > 40:
                print("No Parcel With ID: %s Exist..." % userChoice)

            # If user enters a number less than 1
            # they will receive an error informing them
            # that a parcel with that id does not exist
            if userChoice < 1:
                print("No Parcel With ID: %s Exist..." % userChoice)
            else:
                print(hash_table.search(userChoice))
                print()

        # --- USER CHOICE == 2 -----------------------------------------------------------------------------------------------

        # When the user enters '2' as their choice, they will receive
        # a prompt that will ask them to enter a specific time
        # in the formate -> HH:MM:SS to view all parcels at a specific time
        elif userChoice == 2:
            print('Enter a time: (HH:MM:SS)')

            # Get user input and store in
            # 'userChoice' variable
            userChoice = input()

            (hours, minutes, seconds) = userChoice.split(':')
            input_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

            print('-----------------------------------------------\n')
            print('Viewing All Parcels at time: ', input_time)
            print('-----------------------------------------------')
            for parcel_id in range(1, 41):
                parcel = hash_table.search(parcel_id)
                print(parcel.ReturnParcelPosition(input_time))
            print()

        # --- USER CHOICE == 3 -----------------------------------------------------------------------------------------------

        # If user enter '3' the program will close
        # User will be able to continually view parcels
        # until they enter the number '3'
        elif userChoice == 3:
            print("Exiting program...")


# --- DISTANCE BETWEEN TWO ADDRESSES -----------------------------------------------------------------------------------------------
# This function gets the distance between two address (Address A, Address B)
# Returns distance between two locations
# Time Complexity -> O(1)
def AddressDistances_BetweenTwoPoints(
        addressA,
        addressB,
        address_info,
        distance_info
):
    # Initial distance (0)
    distance = 0
    Address_A = address_info.index(addressA)
    Address_B = address_info.index(addressB)

    # If value empty switch indexes
    if distance_info[Address_A][Address_B] == '':
        distance = distance_info[Address_B][Address_A]
    else:
        distance = distance_info[Address_A][Address_B]

    # Return distance (float data type)
    return float(distance)


# --- SHORTEST DISTANCE -----------------------------------------------------------------------------------------------
# Nearest address to starting address the 'WGUPS Hub'
# Time Complexity -> O(N)
def ShortestDistance(
        address_now,
        parcel_list,
        hash_table,
        address_csv_info,
        distance_csv_info
):
    # initial shortest distance
    shortestDistance = 1000
    # Initial stop (address)
    next_stop = ''
    # Initial parcel id
    next_parcel_id = 0

    # Locate the shortest distance through parcel list
    for parcel_id in parcel_list:
        parcel = hash_table.search(parcel_id)
        address2 = parcel.address

        distance = AddressDistances_BetweenTwoPoints(
            address_now,
            address2,
            address_csv_info,
            distance_csv_info
        )

        # If address is 0, then assign as next address
        if distance == 0:
            # Shortest distance
            shortestDistance = distance

            # Next Address
            next_stop = address2

            # Next Parcel
            next_parcel_id = parcel.parcel_id

            return next_stop, next_parcel_id, shortestDistance
        elif distance < shortestDistance:

            # Shortest distance
            shortestDistance = distance

            # Next Address
            next_stop = address2

            # Next Parcel
            next_parcel_id = parcel.parcel_id

    return next_stop, next_parcel_id, shortestDistance


# --- LOAD PARCELS TO TRUCK -----------------------------------------------------------------------------------------------

def ParcelsToTruck(
        delivery_truck1,
        delivery_truck2,
        delivery_truck3
):
    # Delivery Truck 1 Object (Manually Load Parcels)
    # ** 13, 15, 19 must be delivered together
    deliveryTruck1_Parcels = [
        1, 2, 5, 7, 10, 13, 14, 15, 16, 19, 20, 29, 33, 34, 37, 39
    ]

    # Delivery Truck 2 Object (Manually Load Parcels)
    deliveryTruck2_Parcels = [
        3, 6, 8, 11, 12, 18, 23, 25, 27, 30, 31, 35, 36, 38, 40
    ]

    # Delivery Truck 3 Object (Manually Load Parcels)
    deliveryTruck3_Parcels = [
        4, 9, 17, 21, 22, 24, 26, 28, 32
    ]

    delivery_truck1.truck_parcels = deliveryTruck1_Parcels
    delivery_truck2.truck_parcels = deliveryTruck2_Parcels
    delivery_truck3.truck_parcels = deliveryTruck3_Parcels


# --- PARCEL DELIVERY -----------------------------------------------------------------------------------------------

def DeliverParcels(
        delivery_truck,
        time,
        hash_table,
        address_data,
        distance_data
):
    Parcel_delivered = []  # Empty List
    # Parcel that have not been delivered yet go into a list
    Parcel_not_delivered = delivery_truck.truck_parcels.copy()
    Address_now = delivery_truck.location

    # Total mileage at the start
    Mileage = 0

    # Time object
    Delivery_start = time
    hours, minutes, seconds = Delivery_start.split(':')
    time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

    # Continues to deliver parcels until
    # the 'Parcel_not_delivered' list is empty (0)
    while len(Parcel_not_delivered) > 0:
        for parcel in Parcel_not_delivered:
            Parcel_now = hash_table.search(parcel)
            Parcel_now.status = 'En route'

        for parcel in Parcel_not_delivered:
            address, parcel_id, mileage = ShortestDistance(
                Address_now,
                Parcel_not_delivered,
                hash_table,
                address_data,
                distance_data
            )
            Address_now = address
            Mileage += mileage

            if mileage == 0:
                Parcel_now = hash_table.search(parcel_id)
                Parcel_now.status = 'Delivered at ' + str(time)
            else:
                # Calculate mileage (divide by speed of truck -> 18)
                time_passed = (mileage / 18) * 60 * 60
                dateTimeSecond = datetime.timedelta(seconds=int(time_passed))
                time += dateTimeSecond

                Parcel_now = hash_table.search(parcel_id)
                Parcel_now.status = 'Delivered at ' + str(time)

            # Appends delivered parcel to 'Parcel_delivered' list
            Parcel_delivered.append(parcel_id)
            Parcel_now = hash_table.search(parcel_id)
            Parcel_now.deliveryTruck_Departure = delivery_truck.departure
            Parcel_now.delivery_time = time

            # Once delivered, parcel is removed from
            # 'Parcel_not_delivered' list
            Parcel_not_delivered.remove(parcel_id)

            # Refresh delivery truck location
            delivery_truck.location = Address_now
            delivery_truck.time = time
            delivery_truck.mileage = Mileage

    # After delivery all parcels, delivery truck returns
    # WGUPS Hub
    WGUPSHub = '4001 South 700 East'  # Western Governors University (WGUPS HUB)

    mileage = AddressDistances_BetweenTwoPoints(
        delivery_truck.location,
        WGUPSHub,
        address_data,
        distance_data
    )
    # Gets mileage between current location of truck
    # and WGUPS Hub
    Mileage += mileage
    delivery_truck.mileage = Mileage
    time_passed = (mileage / 18) * 60 * 60
    dateTimeSecond = datetime.timedelta(seconds=int(time_passed))
    time += dateTimeSecond
    # Delivery truck time refreshed
    delivery_truck.time = time
    # Delivery truck location refreshed
    delivery_truck.location = WGUPSHub

    # Returns delivery truck mileage
    return delivery_truck.mileage


# --- USER INTERFACE -----------------------------------------------------------------------------------------------
# This section displays the main user interface, where the user can select
# between three options.
# - Option 1 allows the user to view a single parcels information
# - the user must enter a number between 1 - 40 this is the parcels
# - unique ID number and will be used to retrieve the specific
# - parcels information

# - Option 2 allows the user to view all parcel status by a certain
# - time. The user must enter their desired time in the format
# - (HH:MM:SS) Hours, minutes, and seconds
# - The user will now be able to view the parcels associated id number
# - along with delivery trucks departure time and the parcel's status
# - the status should be one of the following, 'At WGUPS Hub', 'Out For Delivery' or
# - 'Parcel Delivered at (HH:MM:SS)'

# - Option 3 allows the user to simply exit (terminate) the program
def UI(delivery_truck1,
       delivery_truck2,
       delivery_truck3,
       hash_table
       ):
    # This variable will be used to store the user input when selecting
    # a navigation option. This variable is initially set to "" (nothing)
    # until it receives an input from the user
    userChoice = ""

    # Print total mileage for all delivery trucks combined
    total_miles = delivery_truck1.mileage + delivery_truck2.mileage + delivery_truck3.mileage

    # While userChoice does not equal 3 (Exit program)
    # load welcome header and options
    while userChoice != 3:

        # Welcome Header
        print("-" * 100)
        print("---------------------------------- WGUPS PARCEL DELIVERY TRACKING ----------------------------------\n")

        print('* Total Delivery Truck Mileage: %.1f miles' % total_miles)
        print('Truck Mileage Breakdown:\n'
              ' - Delivery Truck 1: %.1f miles\n' % delivery_truck1.mileage,
              '- Delivery Truck 2: %.1f miles\n' % delivery_truck2.mileage,
              '- Delivery Truck 3: %.1f miles' % delivery_truck3.mileage)

        print('-----------------------------------------------\n')
        print('* Please Select From The Following Options Below')
        print('-----------------------------------------------\n')
        print('* (Enter) 1: To View A Specific Parcel [1-40]\n')
        print('* (Enter) 2: To View All Parcels By Time\n')
        print('* (Enter) 3: Exit Program\n')
        print("-" * 100)

        userChoice = int(input())

        # --- USER CHOICE == 1 -----------------------------------------------------------------------------------------------

        # When the user enters '1' as their choice, they will
        # receive a prompt asking them to enter
        # a parcel number to view a specific parcel
        if userChoice == 1:
            print('Enter a Parcel ID number 1-40')

            # Store user input in variable called 'userChoice'
            userChoice = int(input())

            # If user enters a number greater than 40
            # they will receive an error informing them
            # that a parcel with that id does not exist
            if userChoice > 40:
                print("No Parcel With ID: %s Exist..." % userChoice)

            # If user enters a number less than 1
            # they will receive an error informing them
            # that a parcel with that id does not exist
            if userChoice < 1:
                print("No Parcel With ID: %s Exist..." % userChoice)
            else:
                print(hash_table.search(userChoice))
                print()

        # --- USER CHOICE == 2 -----------------------------------------------------------------------------------------------

        # When the user enters '2' as their choice, they will receive
        # a prompt that will ask them to enter a specific time
        # in the formate -> HH:MM:SS to view all parcels at a specific time
        elif userChoice == 2:
            print('Enter a time: (HH:MM:SS)')

            # Get user input and store in
            # 'userChoice' variable
            userChoice = input()

            (hours, minutes, seconds) = userChoice.split(':')
            input_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

            print('-----------------------------------------------\n')
            print('Viewing All Parcels at time: ', input_time)
            print('-----------------------------------------------')
            for parcel_id in range(1, 41):
                parcel = hash_table.search(parcel_id)
                print(parcel.ReturnParcelPosition(input_time))
            print()

        # --- USER CHOICE == 3 -----------------------------------------------------------------------------------------------

        # If user enter '3' the program will close
        # User will be able to continually view parcels
        # until they enter the number '3'
        elif userChoice == 3:
            print("Exiting program...")


# --- USER INTERFACE (CONTINUED) -----------------------------------------------------------------------------------------------

# User Interface
# Time Complexity -> O(N^2)
# Main function
def main():
    parcelHashTable = HashTable.CreateHashTable()

    distance_info = []  # Empty List
    address_info = []  # Empty List

    # Read information from "Package.csv",
    # Read information from "Distance.csv"
    # Read information from "Address.csv"
    Read_csvFile.read_parcel_csv('Package.csv', parcelHashTable)
    Read_csvFile.read_distance_csv('Distances.csv', distance_info)
    Read_csvFile.read_address_csv('Address.csv', address_info)

    WGUPSHub = '4001 South 700 East'  # Western Governors University (WGUPS HUB)
    deliveryTruckParcelList_A = []  # Delivery Truck 1 Empty List
    deliveryTruckParcelList_B = []  # Delivery Truck 2 Empty List
    deliveryTruckParcelList_C = []  # Delivery Truck 3 Empty List

    # Delivery Truck 1
    DeliveryTruck_1 = DeliveryTruckClass.DeliveryTruckClass(
        WGUPSHub,  # Starting Address (WGUPS Hub)
        '08:00:00',
        '08:00:00',
        16, 18, 0,
        deliveryTruckParcelList_A
    )

    # Delivery Truck 2
    DeliveryTruck_2 = DeliveryTruckClass.DeliveryTruckClass(
        WGUPSHub,  # Starting Address (WGUPS Hub)
        '09:05:00',
        '09:05:00',
        16, 18, 0,
        deliveryTruckParcelList_B
    )
    # Delivery Truck 3
    DeliveryTruck_3 = DeliveryTruckClass.DeliveryTruckClass(
        WGUPSHub,  # Starting Address (WGUPS Hub)
        '10:20:00',
        '10:20:00',
        16, 18, 0,
        deliveryTruckParcelList_C
    )

    ParcelsToTruck(DeliveryTruck_1, DeliveryTruck_2, DeliveryTruck_3)
    # Delivery Truck 1
    DeliverParcels(DeliveryTruck_1, DeliveryTruck_1.departure, parcelHashTable, address_info, distance_info)
    # Delivery Truck 2
    DeliverParcels(DeliveryTruck_2, DeliveryTruck_2.departure, parcelHashTable, address_info, distance_info)

    # Parcel 9 address is corrected, Parcel 9 is loaded and out for delivery
    parcel_9 = parcelHashTable.search(9)
    parcel_9.address = '410 S State St'
    # Delivery Truck 3
    DeliverParcels(DeliveryTruck_3, DeliveryTruck_3.departure, parcelHashTable, address_info, distance_info)

    UI(DeliveryTruck_1, DeliveryTruck_2, DeliveryTruck_3, parcelHashTable)


if __name__ == '__main__':
    main()
