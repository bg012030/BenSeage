a = input("Enter an integer: ")
try:
    i = int(a)
    print("valid integer entered:", i)
except ValueError as error:
    print(" poor you , your english is so bad\n",error)