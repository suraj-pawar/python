#!usr/bin/python/python2.7


def armstrong(no):
	add=0
	ans=no	
	while(no>0):
		digit=no%10
		add=add+(digit**3)
		no=no//10

	if(ans==add):
		return True
	return False	


def main():
	input_no=input("Enter the no")
	if armstrong(input_no):
		print "{} no. is armstrong".format(input_no)
	else:
		print "not a armstrong"

if __name__ == "__main__":
	main()
