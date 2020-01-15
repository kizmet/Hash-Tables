# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.items = 0

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        """
        # generate the index
        i = self._hash_mod(key)
        # set var for current pair
        current_pair = self.storage[i]
        # set var for last pair
        last_pair = None
        # loop through pair until find the key
        while current_pair is not None and current_pair.key != key:
            # set the last pair
            last_pair = current_pair
            # point to next pair
            current_pair = last_pair.next
        # if key exists update the value
        if current_pair is not None:
            current_pair.value = value
        # create the new pair
        else:
            new_pair = LinkedPair(key, value)
            # point to current
            new_pair.next = self.storage[i]
            # set new pair at index
            self.storage[i] = new_pair

        self.items += 1

    def remove(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        """
        # call self._hash_mod(key) and get the index of the insertion
        index = self._hash_mod(key)

        # check to see if the value at the index is not None
        if self.storage[index] is not None:
            # set the current pair to the head of the linked list
            current_pair = self.storage[index]

            # if current pair key == key or there is no next pair, set the current index to current_pair next
            if current_pair.key == key or current_pair.next is None:
                self.storage[index] = current_pair.next
                # decrement the count
                self.items -= 1
            # otherwise
            else:
                # loop through the linked list
                while current_pair is not None:
                    # let next pair = current pair next
                    next_pair = current_pair.next

                    # if next pair key == key
                    if next_pair.key == key:
                        # set current pair next to next pair next
                        current_pair.next = next_pair.next
                        # decrement the count
                        self.items -= 1

                    # set current pair to current pair next
                    current_pair = current_pair.next
        # otherwise, print a warning
        else:
            print("Error, key is not there")

        # check to see if the load factor is under 0.2
        if (self.items / len(self.storage)) < 0.2:
            # call self.shrink to halve the size of the hash table's storage
            self.shrink()

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        # find the index of the key
        i = self._hash_mod(key)
        if self.storage[i] != None:
            # entry as the head
            entry = self.storage[i]
            # loop through to find the key
            while entry != None:
                if entry.key == key:
                    # display its value
                    return entry.value
                # set entry to next
                entry = entry.next
            # if key not found
            return None
        # index is none
        else:
            return None

    def resize(self):
        # double the capacity
        self.capacity *= 2
        # reset the item count to zero
        self.items = 0
        # store old storage to put into new storage
        old_storage = self.storage
        # make the new storage
        self.storage = [None] * self.capacity
        current_pair = None
        # loop through each item in old storage
        for i in range(len(old_storage)):
            # set temp variable
            current_pair = old_storage[i]
            # loop through linked list
            while current_pair is not None:
                # insert element
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next

    def shrink(self):
        """
        Halves the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        """
        # halve the size of self.capacity
        self.capacity = int(self.capacity / 2)
        # reset the item count to zero
        self.items = 0
        # let old_storage hold self.storage
        old_storage = self.storage
        # point self.storage to a list of capacity self.capacity
        self.storage = [None] * self.capacity

        # loop through old_storage and rehash every key/value pair
        for item in old_storage:
            # if item is not None
            if item is not None:
                # set the head of the linked list to current_pair
                current_pair = item

                # loop through the linked list
                while current_pair is not None:
                    # call self.insert with the key/value of the linked pair
                    self.insert(current_pair.key, current_pair.value)
                    # set current_pair to current_pair next
                    current_pair = current_pair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
