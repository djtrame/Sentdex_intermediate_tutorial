input_list = range(100)

def div_by_five(num):
    # if num % 5 == 0:
    #     return True
    # else:
    #     return False
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))

abc = [i for i in input_list if div_by_five(i)]

import timeit

#number of seconds this operation takes
#print(timeit.timeit('1+3', number=500000))

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    # if num % 5 == 0:
    #     return True
    # else:
    #     return False
    return num % 5 == 0


xyz = [i for i in input_list if div_by_five(i)]''', number=5000))

#to make the generator = .003301
#to make the list = .085035