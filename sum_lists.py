numList = [4, 5, [1,2], 8, 4, [8, 3, 5]]
def sum1(numList):
    total = 0
    if isinstance(numList, list):
        if numList == []:
            return "The list is empty"
        elif len(numList) == 1:
            for each_num in numList:
                if isinstance(each_num,list):
                    total = total + sum1(each_num[0:])
                else:
                    total = each_num
        else: 
            for each in numList:
                if isinstance(each, list):
                    total = total + sum1(each[0:])
                else:
                    total = total + each
    else:
        return "This is not a list"
    return total
print(sum1(numList))        
