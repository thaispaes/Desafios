def is_square(number):   
    if number < 0:
        return False
    elif number == 0 or number == 1:
        return True
    else:
        for num in range(2, number):  
            divider = number/num
            if divider == num:
                return True
        return False
    
print(is_square(25))            