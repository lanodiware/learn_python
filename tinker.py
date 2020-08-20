def last_digit(lst):
    if lst == []:
        return 1
    p = lst[-2]**lst[-1]
    for i in range(len(lst)-2, 0, -1):
        p = lst[i - 1] ** p
    return str(p)[-1]


print(last_digit([1,2,3,4]))