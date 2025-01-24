class hashtable():  
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

        
    def add_user(self, user, val):
       
        # Get the index from the user
        # using hash function
        hashed_key = hash(user) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == user:
                found_key = True
                break

        #if user already in table update value
        #if not add new user
        if found_key:
            bucket[index] = (user, val)
        else:
            bucket.append((user, val))

    
    def get_user(self, user):
       
        # Get the index from the user using
        # hash function
        hashed_key = hash(user) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key being searched
            if record_key == user:
                found_key = True
                break

        #if user is found return the balance
        #if not raise error
        if found_key:
            return record_val
        else:
            return "No record found"
        

    def del_user(self, user):
       
        # Get the index from the user using
        # hash function
        hashed_key = hash(user) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == user:
                found_key = True
                break

        #if user is found remove from table
        if found_key:
            bucket.pop(index)
        return
    
    