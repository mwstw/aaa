def find_bad_values(a):
    opened_brackets = '[{('
    closed_brackets = ']})'
    brackets_needed_to_find = []
    bad_brackets = []
    i = 0
    while i < len(a):
        # если скобка открывающая, то мы хотим найти для закрывающую
        # поэтому складываем скобки, которые хотим найти, в список
        if opened_brackets.find(a[i]) != -1:
            brackets_needed_to_find.append(closed_brackets[opened_brackets.find(a[i])])
        if closed_brackets.find(a[i]) != -1:
            # если мы нашли скобку в списке тех, которые надо закрыть, то удаляем ее из этого списка
            if a[i] in brackets_needed_to_find:
                j = 0
                while j < len(brackets_needed_to_find):
                    if brackets_needed_to_find[j] == a[i]:
                        del (brackets_needed_to_find[j])
                        break
                    else:
                        j += 1
            # если не нашли скобку, которую надо закрыть, то считаем ее "плохой"
            else:
                bad_brackets.append(a[i])
        i += 1
    # добавляем к списку "плохих" скобок те, для которых не нашлось закрывающих
    for c in brackets_needed_to_find:
        bad_brackets.append(opened_brackets[closed_brackets.find(c)])
    return(bad_brackets)

a = '() ((([]))}'
b = find_bad_values(a)
print(b)

