#!usr/bin/python/python2.7

def turnofrightmost1bit(no):
	x=1
	while (no&x==0):
		x=x<<1
	return (no & ~x)	


# while True
#	if no&x!=0:
#		break
#	x=x<<1
#	return no & ~x

def main():
	input_no=input("ENter the no")
	print turnofrightmost1bit(input_no)

if __name__=="__main__":
	main()
