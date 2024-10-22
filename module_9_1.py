def apply_all_func(int_list, *functions):
    results = {}
    fun = 0
    for fun in functions:
        result = map(functions, int_list)
        print(type(result))
        print(list(result))
    return result





int_list = [11, 1, 3, 4, 9]
print(apply_all_func(int_list, max, min))

