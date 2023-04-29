def create_accumulator(a=0):
    total = 0
    def inner(a):
        nonlocal total
        total +=a
        return total

    return inner

c = create_accumulator(5)

for i in range(5):
    print(i, c(i))

summator_1 = create_accumulator()
print(summator_1(1)) # 1
print(summator_1(5)) # 6
print(summator_1(2)) # 8

summator_2 = create_accumulator()
print(summator_2(3)) #  3
print(summator_2(4)) #  7
