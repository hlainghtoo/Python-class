num1 = int(input("enter unm1: "))
num2 = int(input("enter unm2: "))


choice = input("Enter your choice +, -, *, /: ")



if choice == "+":
    answer= num1 + num2
    print("Answer is ", str(answer))

elif choice == "-":
     answer= num1 - num2
     print ("Answer is ", str(answer))
     
elif choice == "*":
     answer= num1 * num2
     print("Answer is ", str(answer))

elif choice == "/":
     answer= num1 / num2
     print("Answer is ", str(answer))
