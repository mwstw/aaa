def delete_b(a,b):
    i = 0
    while i < len(a):
        if a[i] == b:
            del(a[i])
        else:
            i +=1
    return(a)

a = [1,2,3,1,2,3,4,5,6]
b = 4
a = delete_b(a,b)
print(a)

