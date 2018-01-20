#! usr/bin/python/python2.7



def menu():
	while True:
		print "Menu driven program for Bitwise Operator:\n------------------------------------------------------\n"
		print "1] number is power of 2 \n2] number is multiple of 8\n3] number is multiple of 32 \n4] count number of 1 bits in a given number \n5] Turn Off right most 1 bit\n6] Turn On right most 1 bit \n7] Turn On set off bits \n8] Turn Off set of bits \n9] Toggle set of bits \n10] Swap bits between 2 number for same position \n11] Swap bits between 2 number for different position \n12] Exit\n"	
		
		choice=input("Enter the choice\n")
		if choice>0 and choice<13:
			return choice

# Number is 2's power or not
def powerof2(no):
	return (no & no-1) ==0
	

# number is multiple of 8 
def multipleof8(no):
	return no & 7== 0
	

# number is multiple of 32 
def multipleof32(no):
	return no & 31== 0


# count number of 1 bits in a given number 
def countof1bits(no):
	if no>=1:
		x=1
		count=0
		while x <= no:
			if no & x!=0:
				count+=1
			x=x<<1
		return count
	elif no<0:
		x=-1
		count=0
		while x >= no:
			if no & x!=0:
				count+=1
			x=-x<<1
		return count


# Turn Off right most 1 bit 
def turnoffrightmost1bit(no):
	x=1
	while (no&x==0):
		x=x<<1
	return (no & ~x)	

# Turn On right most 1 bit 
def turnonrightmost1bit(no):
	x=1
	while ((no & x)!=0):
		x=x<<1	
	return (no | x)

# Turn On set off bits 
def turnonsetofbits(no,pos,bits):
		
	x=1
	x=(2**bits)-1
	if bits<=pos:
		x=x<<(pos-bits)
		return no | x



# Turn Off set of bits 
def turnoffsetofbits(no,noofbits,pos):
	x=1
	x=(2**noofbits)-1
	if noofbits<=pos:
		x=x<<(pos-noofbits)
		x=~x
		return no&x
	return -1
			

# Toggle set of bits 
def togglesetofbits(no,pos,bits):
		
	x=1
	x=(2**bits)-1
	if bits<=pos:
		x=x<<(pos-bits)
		return no ^ x

# Swap bits between 2 number for same position 
def swapbits(no1,no2,pos,bits):
	x=no1
	y=no2
	
	mask=((2**bits)-1)<<(pos-bits)   # pos=5,bits=4 ---> 0001 1110
	
	xtemp= x & mask
	ytemp= y & mask

	x=x & (~ mask)
	y=y & (~ mask)

	x=x | ytemp
	y=y | xtemp 

 	return x,y

	
# Swap bits between 2 number for different position 
def swapbitsbetween2differentpos(no1,no2,pos1,pos2,bits):
	x=no1
	y=no2
	
	if pos1 > bits and pos2 >bits :
 
		mask1=((2**bits)-1) << (pos1-bits)
		mask2=((2**bits)-1) << (pos2-bits)

		xtemp=(x & mask1)
		ytemp=(y & mask2)

		x=x & (~mask1)
		y=y & (~mask2)

		if pos1>pos2:
			diff=pos1-pos2
			x=x | (ytemp<<diff)
			y=y | (xtemp>>diff)
		elif pos2>pos1:
			diff=pos2-pos1
			x=x | (ytemp>>diff)
			y=y | (xtemp<<diff)
		else:
			x=x | ytemp
			y=y | xtemp
		
		return x,y
	return -1


#-----------------------------------------------------------------------------------------
def main():
	choice=menu()
	while choice !=12:
		if choice==1:
			input_no=input("Enter the no")
			result=powerof2(input_no)
			if result:
				print "no is of 2's power"
			else:
				print "no is not of 2's power"
			print "\n"	

		elif choice==2:
			input_no=input("Enter the no")
			result= multipleof8(input_no)
			if result:
				print "multiple of 8"
			else:
				print "no is not multiple of 8"
			print "\n"

		elif choice==3:
			input_no=input("Enter the no")
			result= multipleof32(input_no)
			if result:
				print "multiple of 32"
			else:
				print "no is not multiple of 32"
			print "\n"

		elif choice==4:
			input_no=input("Enter the no")
			print countof1bits(input_no)
			print "\n"

		elif choice==5:
			input_no=input("Enter the no")
			print turnoffrightmost1bit(input_no)
			print "\n"

		elif choice==6:
			input_no=input("Enter the no")
			print turnonrightmost1bit(input_no)
			print "\n"

		elif choice==7:
			no=input("Enter the no")
			pos=input("Enter the pos")
			bits=input("Enter the bits")		
			print turnonsetofbits(no,pos,bits)
			print "\n"

		elif choice==8:
			no=input("ENter the no")
			noofbits=input("ENter the no of bits")
			pos=input("Enter the pos")
			print turnoffsetofbits(no,noofbits,pos)	
			print "\n"

		elif choice==9:
			no=input("Enter the no")
			pos=input("Enter the pos")
			bits=input("Enter the bits")		
			print togglesetofbits(no,pos,bits)
			print "\n"

		elif choice==10:
			no1=input("Enter the no1")
			no2=input("Enter the no2")
			pos=input("Enter the pos")
			bits=input("Enter the no of bits")
			print swapbits(no1,no2,pos,bits)
			print "\n"

		elif choice==11:
			no1=input("Enter no1")
			no2=input("Enter no2")
			pos1=input("Enter pos1 for no1")
			pos2=input("Enter pos2 for no2")
			bits=input("Enter no of bits")
			print swapbitsbetween2differentpos(no1,no2,pos1,pos2,bits)
			print "\n"

		choice=menu()


if __name__ == "__main__":
	main()



