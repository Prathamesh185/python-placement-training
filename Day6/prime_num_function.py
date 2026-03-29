def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
n = int(input("Enter a number:"))
if(isPrime(n)):
    print("Number is Prime")
else:
    print("Number is not prime")