def delete_duplicates(a):
   return(list(set(a)))

a = [1,2,3,4,5,1,2]
b = delete_duplicates(a)
print(b)