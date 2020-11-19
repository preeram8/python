numbers = list(input("enter the list of numbers in comma seperated values").split(","))

#numbers = (5,10,9,8)
for i in numbers:
    if (i%5==0):
        print(i)