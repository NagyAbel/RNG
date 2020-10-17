import random 
print("Welcome to RNG (Ranom Number Generator)")
number1   = input("Smallest possible number:")
number2  = input("Largest possbile number:")

if number1 > number2:
    print("The first number can't be bigger then the second one")
else:
    infinite = input("How many random numbers to generate?(0- for infinite)")

    try:
       
           
        if int(infinite) > 0:
           i = 0
           while i < int(infinite):
               i = i + 1
               rnumber = random.randint(int(number1),int(number2))
               print(rnumber)
              
        else:
            while 1+1 == 2:
                rnumber = random.randint(int(number1),int(number2))
                print(rnumber)
           



    except ValueError:
        print("Please enter a valid numbers")
