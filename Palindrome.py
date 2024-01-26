class Solution(object):
    def isPalindrome(number):
        if number < 0: return False
        numbers = list(map(int, str(number)))
        reverse_num = numbers.copy()
        reverse_num.reverse()
        
        return numbers == reverse_num
    
    print(isPalindrome(1000021))
    
    numbers[len(numbers):0:-1] #Reverse