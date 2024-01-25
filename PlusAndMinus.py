def catch_sign_change(lst):
    count = 0
    if lst == []: return 0
    negative = False if lst[0] >= 0 else True
    positive = False if lst[0] < 0 else True
    
    
    for number in lst:
        if number < 0 and positive == True:
            count += 1
            positive, negative = False, True
            
        elif number >= 0 and negative == True:
            count += 1
            positive, negative = True, False
    
    if count > 0:
        return count
    else:
        return 0

