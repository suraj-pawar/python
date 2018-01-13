#!usr/bin/python/python2.7

#def factorial(no):
#	mul=1
#	for x in range(2,no+1):
#		mul=mul*x
#
#	return mul	

def factorial(number):
	fact=-1
	if number > 0:
		if number < 3:
			fact=number
		else:
			fact=1
			while number !=1:
				fact=fact*number	
				number-=1
	return fact



def main():
	input_no=input("Enter the no")
 	print factorial(input_no)


if __name__ == "__main__":
	main()



