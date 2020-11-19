numbers = list(input("Enter the list of numbers seperated by comma").split(","))
sum=0

for i in numbers:
    sum += int(i)
    print(sum)
