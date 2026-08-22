from enum import Enum
from typing import List


"""
Implement a distributed systems monitoring system, where you can register
new instances, renew their status, and query all live instances, or instance
status by instance ID.


You are given a helper class Clock that provides the following APIs:
- get_current_timestamp(): Returns the current timestamp in Unix Epoch (milliseconds).
- set_alarm(): Sets an alarm to trigger at a specific timestamp.

constraints:

- get_live_instances() and get_instance_status() must both be as fast as possible, optimise for time

- set_alarm() can only set one alarm at any point in time, if an alarm is active, a call to set_alarm() will overwrite the previous alarm

- instance ids provided to you will be unique (actually u can change to int i think i was provided int during my interview)

information:

- renew_instance() may or may not be called with an existing instance id, handle that to your own discretion

- renew_instance() if called with the instance id existing in the monitoring system, will update the ttl based on CURRENT TIMESTAMP (ie. new expiry = current timestamp + ttl)

- on_alarm() is a helper that will be automatically called whenever ur alarm triggers, it may be helpful to you to help perform operations when ur alarm triggers

- you may change the return type of get_live_instances() if it helps you with optimising it for time

class Instance
- id
- ttl


Naive solution:
-Maintain a list of all Instance objects
[Instance1, Instance2, ...]

-init -> Initialise instances : [Instance]
-register_instance -> Instance(id, ttl), append to instances, O(1)
-renew_instance -> Iterate through entire list, find matching id, then set new instance.ttl = ttl + current_time O(N)
-get_live_instances -> Iterate through entire list, append each instance that has not expired to res list [], then return it O(N)
-get_instance_status -> Iterate through entire list, find matching id then return LIVE if current_timestamp < ttl etc O(N)


Better way
-Maintain hashmap instances = {
    id : Instance(id, ttl)
}

-Maintain state of live instances the program runs, then we can return get_live_instances in O(1)
-With a minheap
-Can make use of alarm system
    - For the next instance (need ordering, can use minheap) to be expired, we set alarm for it to expire
    - On alarm(), we keep popping until all the instance object that expired, setting the status for them to be expired
    - Maintain the invariant that everything in the minheap is live
    - Then set new alarm for the new top of the heap and continue
    - How do we handle renew_instance? Need to mutate instance object and reheapify which is O(N)
        - We can just leave the dirty entries within the minheap, and only change state if the popped minheap entry (ttl, id) matches the actual object
        - Push the new entry O(log n)
    - How do we return get_live_instances fast? If the minheap no longer maintains the invariant of what is live
        - Maintain a set of live instances, where every initiated instances will populate first, and only remove from the set when an instance has confirmed to be expired
        - When we renew_instance, we just add back the id to the set

-init -> Initialise instances : [Instance]
-register_instance -> Create new instance object and register entry in instances hashmap, set first alarm to initialise chain
-renew_instance -> Look up instance object instances[id], then set new ttl
-get_live_instances -> 
-get_instance_status -> Look up instance object and directly check TTL compare with current timefor status
-onalarm -> pop all the expired entries i.e. ttl < current_time
    - if ttl matches ground truth (instance object in the dict), change status of instance object to expired, remove from live set
    - elif ttl dont match, just pop and ignore 

"""
import heapq
from typing import List, Tuple

class Status(Enum):
    LIVE = 1
    EXPIRED = 2
    UNINIT = 3


class Clock:
    def get_current_timestamp(self) -> int:
        pass


    def set_alarm(self, timestamp: int) -> None:
        pass

class Instance:
    def __init__(self, id: str, reg_time: int, ttl: int):
        self.id = id
        self.status = Status.LIVE 
        self.expiry = reg_time + ttl # reg_time and ttl dont have to be exposed

class DistributedSystemMonitor:
    def init(self, clock: Clock):
        self.clock = clock
        self.min_heap : List[Tuple[int, int]]  = [] # Contains (ttl, id)
        self.instances : dict[int, Instance] = {} # id - > Instance object
        self.live : set[str] = set()

    def register_instance(self, instance_id: str, ttl: int) -> None:
        """
        Create instance object, 
        populate hashmap, minheap and live set
        """
        new_instance = Instance(id=instance_id, reg_time=self.clock.get_current_timestamp(),ttl=ttl)
        self.instances[instance_id] = new_instance
        heap_entry = (new_instance.expiry, instance_id)
        heapq.heappush(self.minheap, heap_entry)
        self.live.add(instance_id)

        if len(self.live) == 1: # Set the first alarm up
            self.clock.set_alarm(new_instance.expiry)



    def renew_instance(self, instance_id: str, ttl: int) -> None:
        """
        Get instance object from hashmap, change expiry to current_time + ttl
        Push new entry to minheap
        Add id to live set
        """
        instance = self.instances[instance_id]
        instance.expiry = self.clock.get_current_timestamp() + ttl 
        heap_entry = (instance.expiry, instance_id)
        heapq.heappush(self.minheap, heap_entry)
        self.live.add(instance_id)


    def get_live_instances(self) -> set[str]:
        return self.live
        
    def get_instance_status(self, instance_id: str) -> Status:
        """
        If instance_id exists -> Get instance object from hashmap and return status
        else -> return uninitialised status
        """
        if instance_id not in self.instances:
            return Status.UNINIT

        return self.instances[instance_id].status



    def on_alarm(self) -> None:
        """
        pop all the expired entries i.e. ttl < current_time
        - if ttl matches ground truth (instance object in the dict), change status of instance object to expired, remove from live set
        - elif ttl dont match, just pop and ignore 

        -finally set new alarm for the new top of the minheap
        """
        current_time = self.clock.get_current_timestamp()

        while self.minheap and self.minheap[0][0] <= current_time: # Current instance expired already
            # Check groundtruth
            heap_expiry, id = heapq.heappop(self.minheap)
            true_expiry = self.instances[id]

            if heap_expiry == true_expiry: # Matches ground truth
                instance_obj = self.instances[id]
                instance_obj.status = Status.EXPIRED
                self.live.remove(id)

        if self.minheap:
            self.clock.set_alarm(self.minheap[0][0])
            


"""
Answer below
"""

import heapq
from enum import Enum


class Status(Enum):
    LIVE = 1
    EXPIRED = 2
    UNINIT = 3


class Clock:
    def get_current_timestamp(self) -> int:
        pass

    def set_alarm(self, timestamp: int) -> None:
        pass


class Instance:
    def __init__(self, instance_id, expiry):
        self.id = instance_id
        self.expiry = expiry
        self.status = Status.LIVE
        self.version = 0


class DistributedSystemMonitor:
    def __init__(self, clock: Clock):
        self.clock = clock

        # (expiry, sequence, instance_id, version)
        self.min_heap = []

        self.instances = {}
        self.live = set()

        # Unique tie breaker for heap
        self.sequence = 0


    def register_instance(self, instance_id, ttl):
        now = self.clock.get_current_timestamp()
        expiry = now + ttl

        instance = Instance(instance_id, expiry)

        self.instances[instance_id] = instance
        self.live.add(instance_id)

        self._push(instance)
        self._schedule_next_alarm()


    def renew_instance(self, instance_id, ttl):
        # Chosen semantics:
        # unknown ID behaves like register
        if instance_id not in self.instances:
            self.register_instance(instance_id, ttl)
            return

        instance = self.instances[instance_id]

        instance.expiry = self.clock.get_current_timestamp() + ttl
        instance.version += 1
        instance.status = Status.LIVE

        self.live.add(instance_id)

        self._push(instance)
        self._schedule_next_alarm()


    def get_live_instances(self):
        return self.live


    def get_instance_status(self, instance_id):
        if instance_id not in self.instances:
            return Status.UNINIT

        return self.instances[instance_id].status


    def on_alarm(self):
        now = self.clock.get_current_timestamp()

        while self.min_heap and self.min_heap[0][0] <= now:
            expiry, _, instance_id, version = heapq.heappop(
                self.min_heap
            )

            instance = self.instances[instance_id]

            # stale heap entry
            if version != instance.version:
                continue

            # Current expiry really occurred
            instance.status = Status.EXPIRED
            self.live.discard(instance_id)

        self._schedule_next_alarm()


    def _push(self, instance):
        self.sequence += 1

        heapq.heappush(
            self.min_heap,
            (
                instance.expiry,
                self.sequence,
                instance.id,
                instance.version,
            )
        )


    def _schedule_next_alarm(self):
        # Remove stale entries sitting at the top
        while self.min_heap:
            expiry, _, instance_id, version = self.min_heap[0]

            instance = self.instances[instance_id]

            if version == instance.version:
                break

            heapq.heappop(self.min_heap)

        if self.min_heap:
            self.clock.set_alarm(self.min_heap[0][0])
        

