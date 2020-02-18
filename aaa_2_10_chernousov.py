def delete_str(a,b):
    i = 0
    while i < len(a):
        if a[i].find(b) == -1:
            del(a[i])
        i += 1
    return(a)

a = ['abba','abb a','a bba','ab ba']
b = 'bba'
a = delete_str(a,b)
print(a)

