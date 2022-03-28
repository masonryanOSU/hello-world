def isSorted(list_ofElements):
    count = 0
    for i in range(1, len(list_ofElements)):
        if list_ofElements[i - 1] < list_ofElements[i] :
            count +=1;
    if count == len(list_ofElements) - 1:
        return True
    else:
        return False
        
print(isSorted([1, 2, 3, 5, 6, 4]))
