
def countno1fornegativeno(no):
	x=-1
	count=0
	while x >= no:
		if no & x!=0:
			count+=1
		x=-x<<1
	return count
def main():
	input_no=input("Enter the no")
	print countno1fornegativeno(input_no)

if __name__ == "__main__":
	main()	

