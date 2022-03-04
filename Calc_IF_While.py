def main():
    end = False
    while not end:
        art_lay = str(input("Choose which arythmetic operation i should do? \n +,-,*,/,% \n"))
        x = int(input("Insert first number: \n"))
        y = int(input("Insert secound number: \n"))
        
        if art_lay == '+':
            print("Score of your count is:", x + y)
        elif art_lay == '-':
            print("Score of your count is:", x - y)
        elif art_lay == '*':
            print("Score of your count is:", x * y)
        elif art_lay == '/':
            print("Score of your count is: ", x / y)
        elif art_lay == '%':
            print("Score of your count is: ", x % y)
        else:
            print("Operation Error, Let's try again!")
            return main()
        print("\n Could You count again? \n If Yes press 't' if not press 'n'")
        
        next_c = input()
        if next_c == "t":
            next_c = False
        elif next_c == "n":
            print ("End of operation!")
            break
      
if __name__ == "__main__":
    main()
