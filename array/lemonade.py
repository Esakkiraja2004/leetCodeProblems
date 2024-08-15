def lemonadeChange(bills):

        fiveCount, tenCount = 0, 0
        for bill in bills:
            if bill == 5:
                fiveCount += 1
            else:
                # could be 10 or 20
                if bill == 10:
                    fiveCount -= 1
                    tenCount += 1
                    if fiveCount < 0:
                        return False
                else:
                    # bill == 20
                    if tenCount > 0:
                        if fiveCount > 0:
                            tenCount -= 1
                            fiveCount -= 1
                        else:
                            return False
                    else:
                        if fiveCount >= 3:
                            fiveCount -= 3
                        else:
                            return False
        return True

bills = [5,5,5,10,10,20]
print(lemonadeChange(bills))