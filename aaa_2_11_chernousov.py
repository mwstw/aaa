def delete_bad_values(a):
    i = 0
    while i < len(a):
        c = a[i].split(',')
        if float(c[0])>90 or float(c[0])<-90 or float(c[1])>180 or float(c[1])<-180:
            del a[i]
        i += 1
    return(a)

a = ['100.0,90.0','50.0,50.0','-190.0,50.0','0.0,-50.0']
a = delete_bad_values(a)
print(a)

