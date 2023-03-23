def mean(arr):
     
    for n in arr:
        # print(isinstance(n,int) , isinstance(n,float))
        if not isinstance(n,int) and not isinstance(n,float):
            return f'The number {n} is neither int nor float'
    total = 0
    # for n in arr:
    #     total+=n
    total =sum(arr)
    return(total/len(arr))

avg=mean(list(range(0,100)))
print(avg)