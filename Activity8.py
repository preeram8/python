numbers=list(input("Enter list of numers"))
a=str(numbers)
print('The given numbers are ' + a)
x=numbers[0]
y=numbers[-1]
if x==y:
    print("True")
else:
    print("False")