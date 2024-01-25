"""HashMaps"""

# Separate Chaining
#  - values append onto a linked list

# Open Addressing (Linear Probing)
#  - increment index by one until there is a slot available
# Open Addressing (Quadratic Probing)
# ^^ 1, 4, 9, 16, ...

# Clustering is when a single hash collision causes additional
# hash collisions when there wouldn't have been one without the
# first


# https://www.codecademy.com/courses/learn-data-structures-and-algorithms-with-python/lessons/hash-maps-concepts/exercises/review-concepts
# Hash map: A key-value store that uses an array and a hashing function to save and retrieve values.
# Key: The identifier given to a value for later retrieval.
# Hash function: A function that takes some input and returns a number.
# Compression function: A function that transforms its inputs into some smaller range of possible outputs.

# Recipe for saving to a hash table:
# - Take the key and plug it into the hash function, getting the hash code.
# - Modulo that hash code by the length of the underlying array, getting an array index.
# - Check if the array at that index is empty, if so, save the value (and the key) there.
# - If the array is full at that index continue to the next possible position depending on your collision strategy.

# Recipe for retrieving from a hash table:
# - Take the key and plug it into the hash function, getting the hash code.
# - Modulo that hash code by the length of the underlying array, getting an array index.
# - Check if the array at that index has contents, if so, check the key saved there.
# - If the key matches the one you're looking for, return the value.
# - If the keys don't match, continue to the next position depending on your collision strategy.

from typing import Any, Optional, List, Tuple


class HashMap:
    """Hash Map"""

    # todo:
    # - delete a k, v pair from the map
    # - make DRY code
    # - array is full

    # open addressing linear probing approach

    def __init__(self, array_size: int) -> None:
        self.array_size = array_size
        self.array: List[Optional[Tuple[Any, Any]]] = [None] * array_size

    def __getitem__(self, key: Any) -> Optional[Any]:
        hash_code = self.hash(key)
        arr_idx = self.compressor(hash_code)
        arr_val = self.array[arr_idx]
        if arr_val is None:
            return None

        if arr_val[0] == key:
            return arr_val[1]

        number_collisions = 1
        while arr_val[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_arr_idx = self.compressor(new_hash_code)
            arr_val = self.array[new_arr_idx]
            if arr_val is None:
                return None
            if arr_val[0] == key:
                return arr_val[1]
            number_collisions += 1
        return None

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_code = self.hash(key)
        arr_idx = self.compressor(hash_code)
        arr_val = self.array[arr_idx]
        if arr_val is None:
            self.array[arr_idx] = (key, value)
            return

        if arr_val[0] == key:
            return

        number_collisions = 1
        while arr_val[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_arr_idx = self.compressor(new_hash_code)
            arr_val = self.array[new_arr_idx]
            if arr_val is None:
                self.array[new_arr_idx] = (key, value)
                return
            if arr_val[0] == key:
                self.array[new_arr_idx] = value
                return
            number_collisions += 1
        return

    def hash(self, key: Any, num_collisions: int = 0) -> int:
        """hash an input key"""
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        return hash_code + num_collisions

    def compressor(self, hash_code: int) -> int:
        """compress the hash code into an index to fit in own array"""
        return hash_code % self.array_size

    def assign(self, key: Any, value: Any) -> None:
        """assign the key to an idx and insert into array"""
        self[key] = value

    def retrieve(self, key: Any) -> Any:
        """get the values stored for the given key"""
        return self[key]
