#!usr/bin/python/python2.7

def turnonsetofbits(no,pos,bits):
		
	x=1
	x=(2**bits)-1
	if bits<=pos:
		x=x<<(pos-bits)

		return no | x

def main():
	no=input("Enter the no")
	pos=input("Enter the pos")
	bits=input("Enter the bits")		

	print turnonsetofbits(no,pos,bits)
	

if __name__=="__main__":
	main()
