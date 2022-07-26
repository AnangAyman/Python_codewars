def comp(array1, array2):
    result=[]
    print(array1, array2)
    if array1 ==None or array2 ==None or (len(array1)!=len(array2)):
        return False
    for item in array1:
        print(item)
        if item*item in array2:
            array2.remove(item*item)
            result.append(True)
        else:
            result.append(False)
    return True if False not in result else False
