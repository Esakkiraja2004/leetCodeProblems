class Solution(object):
    def calPoints(self, operations):
        nl=[]
        for i in operations:
            if i.isnumeric() or i[0]=="-":
                nl.append(int(i))
            elif i=="C":
                nl.pop()
            elif i=="D":
                nl.append(nl[-1]*2)
            elif i=="+":
                nl.append(nl[-1]+nl[-2])
            # elif i[0]=="-":
            #     nl.append(int(i))
        return sum(nl) 