"""
Design hashmap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Intuition : Hash using modulo operator, then use linkedlists for chaining.
"""



class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashed_array = [ListNode(key=None, val=None) for _ in range(1000)] # size of 1000

    def put(self, key: int, value: int) -> None:
        hash_val = key % 1000
        dummy = self.hashed_array[hash_val]
        # look for existing key, otherwise append to end of linked list
        cur = dummy
        prev = None
        while cur:
            if cur.key == key:
                cur.val = value
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key=key, val=value)
        return

    def get(self, key: int) -> int:
        hash_val = key % 1000
        dummy = self.hashed_array[hash_val]
        cur = dummy
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
                    
    def remove(self, key: int) -> None:
        hash_val = key % 1000
        dummy = self.hashed_array[hash_val]
        cur = dummy
        prev = None
        while cur:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return
            prev = cur
            cur = cur.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)