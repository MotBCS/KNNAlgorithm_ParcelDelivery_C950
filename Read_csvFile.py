# - Mya Thomas
# - ID: 010507144

# - C950 Data Structures and Algorithms II
# ----------------------------------------------------------------------------------------------------------------------

# Imports
import csv
from Parcel import ParcelClass


# --- READ PARCEL CSV FILES ----------------------------------------------------------------------
# Read Parcel csv file
# Time Complexity -> O(N)
def read_parcel_csv(csv_file, hash_table):

    with open(csv_file) as parcel_csv:
        parcel_info = csv.reader(parcel_csv, delimiter=',')

        # Insert values from csv file
        # into key_value pair in the
        # hash table
        # Time Complexity -> O(N)
        for parcel in parcel_info:
            parcel_id = int(parcel[0])
            parcel_address = parcel[1]
            parcel_city = parcel[2]
            parcel_state = parcel[3]
            parcel_postalCode = parcel[4]
            parcel_deadline = parcel[5]
            parcel_weight = float(parcel[6])
            parcel_status = 'At WGUPS hub'

            # Parcel Object
            parcelObject = ParcelClass(
                parcel_id,
                parcel_address,
                parcel_city,
                parcel_state,
                parcel_postalCode,
                parcel_deadline,
                parcel_weight,
                parcel_status
            )
            # Insert parcel id and parcel object
            # into hash table
            hash_table.insert(
                parcel_id,
                parcelObject
            )


# --- PRINT HASH TABLE (PARCELS) ----------------------------------------------------------------------
# Time Complexity -> O(N)
def printHashTable(hash_table):

    for i in range(len(hash_table.table)):
        print("{}".format(hash_table.search(i + 1)))


# --- READ ADDRESS CSV FILES ----------------------------------------------------------------------
# Time Complexity -> O(N)
# Read Address csv file
def read_address_csv(csv_file, address_info):

    with open(csv_file) as address_csv:
        addresses = csv.reader(address_csv, delimiter=",")
        for address in addresses:
            address_info.append(address[2])


# --- READ DISTANCE CSV FILES ----------------------------------------------------------------------
# Time Complexity -> O(N)
# Read Distance csv file
def read_distance_csv(csv_file, distance_info):

    with open(csv_file) as distance_csv:
        distances = csv.reader(distance_csv, delimiter=",")
        for distance in distances:
            distance_info.append(distance)
