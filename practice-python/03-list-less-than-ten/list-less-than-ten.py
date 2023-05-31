def elems_less_than_n(l, num):
    res = []
    for elem in l:
        if elem < num:
            res.append(elem)
    return res

def elems_less_than_n_list_comprehension(l, num):
    return [elem for elem in l if elem < num]

def elems_less_than_n_filter(l, num):
    return list(filter(lambda x: x < num, l))

exercise_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Say a number: "))

print(elems_less_than_n_filter(exercise_list, number))
