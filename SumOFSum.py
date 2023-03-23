def sum_of_sum(arr):
    # print(sum(arr))
    
    total =0
    for a in arr:
        if not isinstance(a, int) and not isinstance(a,float):
            print (f'the {a} is string')
        s=str(a)
        if len(s)>1:
            print(s,list(s))
            l=list(map(int,s))
            total+=sum(l)
            # newl=[]
            # for sn in l:
            #     newl.append(int(sn))
            # total+=sum(newl)
        else:
            total+=a
    return(total)

sos=sum_of_sum([2,'31',5,341])
print(sos)