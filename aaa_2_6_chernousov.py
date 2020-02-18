def count_non_unique(a):
    values = list()
    non_unique_values = list()
    for i in a:
        if i not in values:
            values.append(i)
        else:
            non_unique_values.append(i)
    return(len(set(non_unique_values)))

a = [1,2,3,1,2,3,4,5,6]
b = count_non_unique(a)
print(b)

