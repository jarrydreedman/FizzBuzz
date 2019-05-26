#!python3
# fizzbuzz.py - classic fizzbuzz example. Will ask for and take input on range and then run fizzbuzz function
import os

startRange = 0

def main():
    global startRange
    print("Please choose the number range to run fizzbuzz through")
    print("Number one: ")
    startRange = input()
    checkInput(startRange)
    startRangeInt = int(startRange)      
    print("Number two: ")
    endRange = input()
    checkInput(endRange)
    endRangeInt = int(endRange)
    print("Now processing FizzBuzz...")
    print("The numbers between: " + startRange + " and " + endRange + " will be FizzBuzzed\n " + "If the number is divisible by 3, it is Fizz\n " + "If the number is divisible by 5, it is Buzz\n " + "and if it is divisible by both, FizzBuzz")
    n = 0
    for n in range(startRangeInt, endRangeInt):
        print(fizzbuzz(n))


def checkInput(inputData):
    while True:
        try:
            val = int(inputData)
            print("Yes input string is an Integer.")
            print("Input number value is: ", val)
            break
        except ValueError:
            print("not integer, try again")
            os.system('clear')
            main()
            break
    else:
        print("try again")
        return False
      
def fizzbuzz(number):
    number = int(number)
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"        
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

if __name__ == "__main__":
    main()
    #test()

