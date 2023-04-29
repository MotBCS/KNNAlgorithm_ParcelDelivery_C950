# - Mya Thomas
# - ID: 010507144

# - C950 Data Structures and Algorithms II

# --- HASH TABLE CLASS ----------------------------------------------------------------------

# Ref: zyBook: Figure 7.8.2 Hash Table using chaining

# Hash table class using linear chaining
# Assigns all 'buckets' with an empty list
# (Object)
class CreateHashTable:
    # Set hash table size to 40
    # Time Complexity -> O(N)
    def __init__(self, initial_capacity=40):
        # Empty List
        self.table = []

        for i in range(initial_capacity):
            self.table.append([])

    # --- INSERT/UPDATE INTO HASH TABLE -----------------------------------------------------------------------------------------------

    # Inserts a new item into hash table
    # Time Complexity -> O(N)
    def insert(self, key, item):
        # Get the list where the inserted item will reside
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Time Complexity -> O(N)
        # Updates key if it already exists
        for kv in bucket_list:

            # return (key value)
            if kv[0] == key:
                kv[1] = item
                return True
        # If no key found, new item will be added
        # to the end of the list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # --- SEARCH HASH TABLE -----------------------------------------------------------------------------------------------

    # Searches for item in hash table
    # Time Complexity -> O(N)
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

        # Return 'None' if not found
        return None

    # --- REMOVE ITEM FROM HASH TABLE -----------------------------------------------------------------------------------------------

    # Remove item from hash table
    # Time Complexity -> O(N)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # If key is found, then remove item from
        # hash table
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
                return print('Parcel ', key, ' has been delete from table')
        # If no item to remove is found return 'None'
        return None