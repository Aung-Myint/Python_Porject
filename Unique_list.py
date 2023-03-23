def uinque(arr,ignore=True):
    target_arr = []
    new_arr=[]

    if ignore:

        for item in arr:
            if isinstance(item,int):
                target_arr.append(item)
    else:
        target_arr=arr

    # print(target_arr)
    for item in target_arr:
        if item in new_arr:
            continue
        else:
            new_arr.append(item)
    return(new_arr)




unq1=uinque([1,1,3,4,3,1,"hello","hello","world"])
print(unq1)
unq2=uinque([1,1,3,4,3,1,"hello","hello","world"],ignore=False)
print(unq2)

