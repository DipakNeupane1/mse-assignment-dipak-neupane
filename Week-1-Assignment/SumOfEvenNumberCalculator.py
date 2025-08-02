def calculateSum(number):
    sum=0;
    if number<=0:
        return print("Given number is 0 or negative, so please enter positive number for sum calculation.")
    else:
        i=1;
        while i <=number:
         if i % 2 == 0:
           sum+=i
         i+=1
    return sum

if __name__ == "__main__":
  number = int(input("Please enter a number of your choice: "))
  print(f"The sum of even numbers between 1 to {number} is {calculateSum(number)}")