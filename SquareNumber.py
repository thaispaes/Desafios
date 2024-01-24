def is_square(number):   
    if number == 0 or number == 1:
        return True
    else:
        for num in range(2, number): 
            if number/num == num:
                return True
        return False