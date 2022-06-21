## Method 1

n=int(input("Enter the number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")


## ***********************************************************************************************************


## Method 2 

def isodd(num):
    return num&1

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if isodd(num):
        print("odd")
    else:
        print("Even")