def multiply(a=1):

    def inner(x=1):
        return a*x

    return inner


f_2 = multiply(2)
print("2 x 5 =", f_2(5)) #10
print("2 x 15 =", f_2(15)) #30
f_3 = multiply(3)
print("3 x 5 =", f_3(5)) #15
print("3 x 15 =", f_3(15)) #45
