def multipleOf(number):
    totalMultiples = int(0)
    
    for num in range(number, 0, -1):
        if num == number:
            continue 
        
        is_treeMultiple = int(num) % 3 == 0
        is_fiveMultiple = int(num) % 5 == 0 
        
        if is_fiveMultiple == True and is_treeMultiple == True:
            totalMultiples += num
        else:
            if is_fiveMultiple == True:
                totalMultiples += num
            elif is_treeMultiple == True:
                totalMultiples += num
            
    return totalMultiples

def solution(maxNumber):
   return multipleOf(maxNumber)

solution(6)