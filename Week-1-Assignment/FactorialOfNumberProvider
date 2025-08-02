def calculateFactorial(number):
 n=int(number)
 if n<0:
    print("Given number {number} is negative and not allowed.")
 elif n==0:
     return 1;
 else:
    return n * calculateFactorial(n - 1) # Keep calling the same funtion/method until n==0 and returns 1 at last.

#Defining main method, take input from user and call calculateFactorial method defined above.
if __name__ == "__main__":

# Getting input of number 'n' to get factorial of it and caste it into integer type.
    number = int(input("Please enter a number of your choice: "))
    print(f"The factorial of {number} is {calculateFactorial(number)}")