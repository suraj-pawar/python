#!usr/bin/python/python2.7


def divisibleby32(no):
	return no & 31 ==0

def main():
	input_no=input("Enter the no")
	result=divisibleby32(input_no)

	if result:
		print "is divisible by 32"
	else:
		print "is not divisible by 32"	


if __name__ == "__main__":
	main()


