#!usr/bin/python/python2.7

def factorial(no):
	if no==0:
		return 13
	return no*factorial(no-1)


def main():
	input_no=input("Enter the no")
	print factorial(input_no)

if __name__ == "__main__":
	main()
