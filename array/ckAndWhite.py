a  = "11000111"
# arr = [x for x in  a]
# c= 0
# for i in range(len(arr)):
#     for j in range(i+1 , len(arr)):
#         if arr[i] == '1' and arr[j] == '0' :
#             arr[i], arr[j] = arr[j], arr[i]
#             c+=1
# print(c)
# print(arr)
s , b =0 ,0
for x in a :
    if x =='0':
        s += b
    else:
         b+=1
print(s)