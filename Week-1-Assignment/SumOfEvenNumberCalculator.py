def calculateSum(number):
    sum=0;
    sumOfOdd=0;
    if number<=0:
        return print("Given number is 0 or negative, so please enter positive number for sum calculation.")
    else:
        i=1;
        while i <=number:
         if i % 2 == 0:
           print("Even number is ::", i)
           sum+=i
         else:
            print("Odd number is :: ", i)
            sumOfOdd+=i
         i+=1
    print(f"Sum of odd numbers between 1 to {number} is :: ", sumOfOdd)
    return sum

if __name__ == "__main__":
  number = int(input("Please enter a number of your choice: "))
  print(f"The sum of even numbers between 1 to {number} is {calculateSum(number)}")