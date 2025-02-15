#TYRON SEBASTIAN 
#LABORATORY009

def main():
    
    user_input = input("Enter a number: ")
    number = int(user_input)
    if number % 2 == 0:
        print("The number", number, "is Even.")
    else:
        print("The number", number, "is Odd.")
    try:
        #code here
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
    

