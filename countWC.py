#!usr/bin/python/python2.7

def main():
	input_str=input("Enter the string")
	count=len(input_str.split(" "))
	length=len(input_str)
	print "total no. of words = %d"%count

	print "total no. of characters = %d"%length
		
if __name__ == "__main__":
	main()
