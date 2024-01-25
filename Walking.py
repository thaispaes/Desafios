def verify_route(walk):
    north, east = 0, 0
    if len(walk) == 10:
        for direction in walk:
            if direction == 'n': north+=1
            if direction == 's': north-=1
            if direction == 'w': east-=1
            if direction == 'e': east+=1
        if north == 0 and east == 0:
            return True
    else:
        return False
    
def is_valid_walk(walk):
    if walk == []: return False
    
    for direction in walk:
        if len(walk) == 10 and verify_route(walk) == True:
            return True 
        
        if len(walk) <10 or len(walk) >10:
            return False
        
        else:
            return False
        
lista = ['s', 'e', 'w', 'n', 'w', 's', 'e', 'w', 'n', 's']  
print(is_valid_walk(lista))