def verify_duplicates(walk):
    for direction in range(len(walk)):
        if walk[direction] == walk[direction+1]:
            return True
        else:
            return False
       
def is_valid_walk(walk):
    if walk == []: return False
    
    
    for direction in walk:
        if len(walk) == 10 and verify_duplicates(walk) == False:
            return True 
        
        else:
            return False
        
