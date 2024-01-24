
def factory(number):
    def numbers(numberArray):
        array = []
        for num in numberArray:
            array.append(num * number)
        return array
    return numbers