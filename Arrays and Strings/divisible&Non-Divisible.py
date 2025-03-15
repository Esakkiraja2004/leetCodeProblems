n  = 10
m = 3
num1 = []
num2 =[]
for i in range(1,n+1):
    if i%m != 0:
        num1.append(i)
    else:
        num2.append(i)
print(sum(num1) - sum(num2))