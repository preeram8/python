fruit_shop = {
    "apple" : 10,
    "banana" : 5,
    "mango" : 20
}

A = input("What fruit are you looking for ").lower()

if (A in fruit_shop):
        print("Yes, this is available")
	
else:
	
    print("No, this is not available")