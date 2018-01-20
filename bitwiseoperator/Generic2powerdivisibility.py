#! usr/ibn/python/python2.7

def Generic2powerDivisibilityTest(no,divisor):
	return (no & (divisor-1))==0

def checknois2power(no):
	return no & no-1==0

def main():
	no=input("Enter the no")
	result=checknois2power(no)
	
	if result:
		divisor=input("ENter the divisor")
		print Generic2powerDivisibilityTest(no,divisor)
	else:
		print "given number is not 2's power"


if __name__ == "__main__":
	main()
