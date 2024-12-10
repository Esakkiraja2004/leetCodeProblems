n = 5
res = [[1]]
for i in range(n-1):
    temp = [0] + res[-1] + [0]
    print("value created")
    print(temp)
    print("result")
    temp_res =[]    
    for i in range(len(temp)-1):
        temp_res.append(temp[i] + temp[i+1])
    res.append(temp_res)
    print(temp_res)


        # Explaination:

        #             value created
        #             [0, 1, 0]
        #             result
        #             [1, 1]
        #             value created
        #             [0, 1, 1, 0]
        #             result
        #             [1, 2, 1]
        #             value created
        #             [0, 1, 2, 1, 0]
        #             result
        #             [1, 3, 3, 1]
        #             value created
        #             [0, 1, 3, 3, 1, 0]
        #             result
        #             [1, 4, 6, 4, 1]
