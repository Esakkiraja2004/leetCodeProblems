def digi(o):
    while o >= 10:  # Repeat the process until the number becomes a single digit
        arr = list(map(int, str(o)))  # Split the number into individual digits
        o = sum(arr)  # Sum the digits
    return o  # Return the single-digit result

print(digi(38))


    # def addDigits(self, num):
    #     while True:
    #         number = [int(number) for number in str(num)]
    #         num = sum(number)

    #         if num >= 10:
    #             continue
    #         else:
    #             return num