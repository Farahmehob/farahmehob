8
def X(m):
    if m==0:
        return 1
    else:
        return m * X(m-1)
num=int(input("Enter a number:"))
if num < 0:
    print("x is not defined")
elif num == 0:
    print("x of 0 is 1")
else:
    Y=X(num)
    print(Y)
