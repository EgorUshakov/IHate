# State human years 
age = float(input("Enter an age in human years"))
print(age)

# State how old they are in dog years
if age < 1:
	print("error")
else:	
	dog = age * 10.5
	print("OMG, that is", dog, "in dog years. That is amazing !!!");  
