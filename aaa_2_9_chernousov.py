def delete_double_spaces(a):
    while a.find('  ') != -1:
        a = a.replace('  ', ' ')
    return(a)

a = '  ab     b c  d   .'
a = delete_double_spaces(a)
print(a)

