from enum import Enum
import config

class hashset:
    def __init__(self):
        # TODO: create initial hash table
        self.verbose = config.verbose
        self.mode = config.mode
        #hashtablesize is the total amount of the place
        self.hashtablesize = config.init_size
        #size is the current amount of the place we hava already put in so the value is 0
        self.size = 0
        self.hashtable = [(None,None) for i in range(self.hashtablesize)]
        self.loadfactor = 0.75
        self.capacity = self.hashtablesize
                
    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i < n):
            if (n % i == 0):
                return False
            i = i + 1
        return True
        
    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n
        
    def hash_operation(self,stringvalue):
        #return the hash value        
        return stringvalue % self.hashtablesize
    
    #THis function will return ASCII value of the string 
    def ord_transfer_operation(self,stringvalue):
        # the ord value we define it as an int and the initial value is 0
        ordvalue = 0 
        for value in range(len(stringvalue)):
            temp = stringvalue[value]
            ordvalue += ord(temp)
        return ordvalue       

    def size(self):
        # TODO return number of values stored in table
        return self.size

    def insert(self, value):
        # TODO code for inserting into  hash table
        #key is the return value of ord_transfer_operation
        key = self.ord_transfer_operation(value)
        hash_key = self.hash_operation(key)
        if self.hashtable[hash_key][0] is None:
            self.hashtable[hash_key] = (key,value)
        #In the else statement there is already a transfer key
        else:
            for i in range(self.capacity):
                if(self.find(value)):
                    break
                hash_key = self.hash_operation(key + i)
                # for key + i ,we use linier hash to insert the value                 
                if self.hash_table[hash_key][0] is None:
                    self.hash_table[hash_key] = (key, value)
        self.size += 1        
        
    def find(self, value):
        # TODO code for looking up in hash table
        key = self.ord_transfer_operation(value)
        hash_key = self.hash_operation(key)
        new_key,new_value = self.hashtable[hash_key]
        # the if statement is we can find it directly
        if (new_key == key and new_value == value):
            return True
        # the else statement is for the linear find method to loop through the current hashtable
        else:
            for i in range(self.capacity):
                hash_key = self.hash_operation(key + i)
                new_key, new_value = self.hashtable[hash_key]
                if (new_key == key and new_value == value):
                    return True 
        #In the last statement is that we can't find the value in our hash map we need to return false           
        return False    
        
    def print_set(self):
        # TODO code for printing hash table
        print(self.hashtable)
        
    def print_stats(self):
        # TODO code for printing statistics
        print("Placeholder")
        
# This is a cell structure assuming Open Addressing
# It should contain and element that is the key and a state which is empty, in_use or deleted
# You will need alternative data-structures for separate chaining
class cell:
    def __init__(self):
        pass
        
class state(Enum):
    empty = 0
    in_use = 1
    deleted = 2
        
# Hashing Modes
class HashingModes(Enum):
    HASH_1_LINEAR_PROBING=0
    HASH_1_QUADRATIC_PROBING=1
    HASH_1_DOUBLE_HASHING=2
    HASH_1_SEPARATE_CHAINING=3
    HASH_2_LINEAR_PROBING=4
    HASH_2_QUADRATIC_PROBING=5
    HASH_2_DOUBLE_HASHING=6
    HASH_2_SEPARATE_CHAINING=7
