x = (i for i in range(5))

#move the selector one index
next(x)
x.__next__()

for i in x:
    print(i)

print('-------------------')


class range_example:
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val

x = range_example(5)


x.__next__()
next(x)
print(x)

for i in range_example(5):
    print(i)

print('-------------------')
def range_generator(end):
    current = 0

    while current < end:
        yield current
        current += 1

for i in range_generator(5):
    print(i)

x = range_generator(5)

for i in x:
    print(i)